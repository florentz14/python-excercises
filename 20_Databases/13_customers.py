import sqlite3
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "Data" / "customers.db"
SQL_PATH = ROOT / "Script_Sql" / "customers.sql"

DB_PATH.parent.mkdir(parents=True, exist_ok=True)


def _needs_seed(conn: sqlite3.Connection) -> bool:
    cur = conn.cursor()
    cur.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='customers'"
    )
    if cur.fetchone() is None:
        return True
    cur.execute("SELECT COUNT(*) FROM customers")
    (n,) = cur.fetchone()
    return n == 0


conn = sqlite3.connect(DB_PATH)

try:
    if _needs_seed(conn):
        conn.executescript(SQL_PATH.read_text(encoding="utf-8"))
        conn.commit()
    customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
    customers_df.to_sql(
        "customers_backup",
        conn,
        if_exists="replace",
        index=False,
    )
    conn.commit()
finally:
    conn.close()

print(f"Rows written to customers_backup: {len(customers_df)}")
print(customers_df.head())
