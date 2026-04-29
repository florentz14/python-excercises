"""
Load and audit PostgreSQL schema/data from a SQL file.

Default behavior is safe audit mode (no SQL execution). Use --apply to run
the SQL file first, then report table row counts and empty tables.
"""

import argparse
import os
from pathlib import Path

import psycopg2
from dotenv import load_dotenv
from psycopg2 import OperationalError, sql

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": int(os.getenv("POSTGRES_PORT", "5432")),
    "dbname": os.getenv("POSTGRES_DB", "finances_db"),
    "user": os.getenv("POSTGRES_USER", "postgres"),
    "password": os.getenv("POSTGRES_PASSWORD", ""),
}

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_SQL_FILE = BASE_DIR / "Script_Sql" / "family_budget_complete.sql"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Load SQL file into PostgreSQL and report empty tables."
    )
    parser.add_argument(
        "--sql-file",
        default=str(DEFAULT_SQL_FILE),
        help="Path to SQL file to execute (default: Script_Sql/family_budget_complete.sql)",
    )
    parser.add_argument(
        "--schema",
        default="public",
        help="Schema to inspect for table counts (default: public)",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Execute the SQL file before auditing tables.",
    )
    return parser.parse_args()


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def execute_sql_file(cursor, sql_file: Path) -> None:
    sql_text = sql_file.read_text(encoding="utf-8")
    cursor.execute(sql_text)


def fetch_base_tables(cursor, schema_name: str) -> list[str]:
    cursor.execute(
        """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = %s
          AND table_type = 'BASE TABLE'
        ORDER BY table_name
        """,
        (schema_name,),
    )
    return [row[0] for row in cursor.fetchall()]


def table_row_count(cursor, schema_name: str, table_name: str) -> int:
    query = sql.SQL("SELECT COUNT(*) FROM {}.{}").format(
        sql.Identifier(schema_name),
        sql.Identifier(table_name),
    )
    cursor.execute(query)
    return cursor.fetchone()[0]


def main() -> int:
    args = parse_args()
    sql_file = Path(args.sql_file).resolve()

    print("=" * 68)
    print("      POSTGRESQL SQL LOADER + EMPTY TABLE AUDIT")
    print("=" * 68)
    print(f"Database : {DB_CONFIG['dbname']}")
    print(f"Host     : {DB_CONFIG['host']}:{DB_CONFIG['port']}")
    print(f"User     : {DB_CONFIG['user']}")
    print(f"Schema   : {args.schema}")
    print(f"SQL file : {sql_file}")

    if not sql_file.exists():
        print("\nERROR: SQL file not found.")
        return 1

    try:
        connection = get_connection()
    except OperationalError as error:
        print(f"\nConnection failed: {error}")
        return 1

    try:
        with connection:
            with connection.cursor() as cursor:
                if args.apply:
                    print("\nApplying SQL file...")
                    execute_sql_file(cursor, sql_file)
                    print("SQL file executed successfully.")
                else:
                    print("\nAudit mode only (no SQL execution).")

                tables = fetch_base_tables(cursor, args.schema)

                if not tables:
                    print("\nNo tables found in target schema.")
                    return 0

                print("\nTable row counts:")
                print("-" * 68)

                empty_tables = []
                for table in tables:
                    count = table_row_count(cursor, args.schema, table)
                    print(f"{table:<45} {count:>10}")
                    if count == 0:
                        empty_tables.append(table)

                print("-" * 68)
                print(f"Total tables: {len(tables)}")
                print(f"Empty tables: {len(empty_tables)}")

                if empty_tables:
                    print("\nTables with NO data:")
                    for name in empty_tables:
                        print(f"- {name}")
                else:
                    print("\nAll tables contain data.")

    finally:
        connection.close()
        print("\nConnection closed.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
