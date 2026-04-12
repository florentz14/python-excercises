# -------------------------------------------------
# File Name: 11_survey.py
# Description: Filter surveys for year 2002 and store them in table surveys2002 (portal.db).
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

    surveys_df = pd.read_sql_query("SELECT * FROM surveys", conn)

    surveys_2002 = surveys_df.loc[surveys_df["year"] == 2002].copy()
    surveys_2002.to_sql(
        "surveys2002",
        conn,
        if_exists="replace",
        index=False,
    )
    conn.commit()
finally:
    conn.close()

print(f"Rows written to surveys2002: {len(surveys_2002)}")
print(surveys_2002.head())
