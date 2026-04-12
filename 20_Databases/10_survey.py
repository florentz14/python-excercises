# -------------------------------------------------
# File Name: 10_survey.py
# Description: Load surveys from SQLite (portal.db) into pandas; seed DB if empty.
# -------------------------------------------------

from pathlib import Path

import pandas as pd
import sqlite3

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "data" / "portal.db"
SQL_PATH = ROOT / "Script_Sql" / "survey.sql"

DB_PATH.parent.mkdir(parents=True, exist_ok=True)


def _needs_seed(conn: sqlite3.Connection) -> bool:
    cur = conn.cursor()
    cur.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='surveys'"
    )
    if cur.fetchone() is None:
        return True
    cur.execute("SELECT COUNT(*) FROM surveys")
    (n,) = cur.fetchone()
    return n == 0


conn = sqlite3.connect(DB_PATH)
try:
    if _needs_seed(conn):
        conn.executescript(SQL_PATH.read_text(encoding="utf-8"))
        conn.commit()

    df = pd.read_sql_query("SELECT * FROM surveys", conn, index_col="id")
finally:
    conn.close()

print("DataFrame (first rows):")
print(df.head())
print()
print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")
print()
print("Column dtypes:")
print(df.dtypes)
print()
print("Year value counts:")
print(df["year"].value_counts().sort_index())
