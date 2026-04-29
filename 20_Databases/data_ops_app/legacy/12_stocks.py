import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "data" / "stocks.db"
SQL_PATH = Path(__file__).parent / "Script_Sql" / "stocks.sql"

DB_PATH.parent.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
try:
    conn.executescript(SQL_PATH.read_text(encoding="utf-8"))
    conn.commit()
finally:
    conn.close()
