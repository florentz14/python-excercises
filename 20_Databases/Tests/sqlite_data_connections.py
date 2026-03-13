# -------------------------------------------------
# File Name: sqlite_data_connections.py
# Author: Florentino Baez
# Date: 12/03/2026
# Description: Test SQLite connections for all databases in 20_Databases/Data.
# -------------------------------------------------

import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "Data"
SQLITE_PATTERNS = ("*.db", "*.sqlite3.db", "*.sqlite3")


def list_sqlite_files() -> list[Path]:
    """Collect unique SQLite database files from Data directory."""
    files: list[Path] = []
    seen: set[Path] = set()
    for pattern in SQLITE_PATTERNS:
        for file_path in DATA_DIR.glob(pattern):
            resolved = file_path.resolve()
            if resolved not in seen:
                seen.add(resolved)
                files.append(file_path)
    return sorted(files)


def test_sqlite_connection(db_path: Path) -> bool:
    """Open SQLite DB, print table list, and close connection."""
    print("=" * 70)
    print(f"Database: {db_path.name}")
    print(f"Path    : {db_path}")
    print("-" * 70)

    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        )
        tables = [row[0] for row in cursor.fetchall()]

        if tables:
            print(f"[OK] Connected. Tables found ({len(tables)}):")
            for table in tables:
                print(f"  - {table}")
        else:
            print("[OK] Connected. No user tables found.")

        cursor.close()
        connection.close()
        print("[OK] Connection closed successfully.\n")
        return True

    except sqlite3.Error as error:
        print(f"[ERROR] SQLite connection failed: {error}\n")
        return False


def main() -> None:
    print("=" * 70)
    print("        SQLITE CONNECTION TEST - 20_Databases/Data")
    print("=" * 70)

    if not DATA_DIR.exists():
        print(f"[ERROR] Data directory not found: {DATA_DIR}")
        return

    db_files = list_sqlite_files()
    if not db_files:
        print(f"[WARNING] No SQLite files found in: {DATA_DIR}")
        return

    print(f"\nFound {len(db_files)} SQLite database file(s).\n")

    success_count = 0
    for db_file in db_files:
        if test_sqlite_connection(db_file):
            success_count += 1

    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Successful connections: {success_count}/{len(db_files)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
