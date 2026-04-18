"""
CSV → SQLite → pandas: cargar un CSV, guardarlo en una tabla y leerlo con SQL.

Desde la raíz del repo:
    python ITSE-1003/Examples/databases/02_pandas_sqlite_csv_roundtrip.py
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT.parent / "data"
CSV_PATH = DATA_DIR / "students_week3.csv"
DB_PATH = DATA_DIR / "students_week3.sqlite.db"


def main() -> None:
    if not CSV_PATH.is_file():
        raise FileNotFoundError(f"No se encontró el CSV: {CSV_PATH}")

    df_csv = pd.read_csv(CSV_PATH)
    print("--- Origen (CSV): shape", df_csv.shape, "---")
    print(df_csv.head(), "\n")

    conn = sqlite3.connect(DB_PATH)
    try:
        # Reemplaza la tabla si ya existe (útil en demos y notebooks).
        df_csv.to_sql("students", conn, if_exists="replace", index=False)

        # Misma información, consultada como si fuera un servidor SQL.
        df_sql = pd.read_sql_query(
            "SELECT Id, Name, Major, Grade FROM students WHERE Grade >= 90 ORDER BY Grade DESC",
            conn,
        )
        print("--- Desde SQLite (Grade >= 90) ---")
        print(df_sql, "\n")

        print(f"SQLite creado/actualizado en: {DB_PATH}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
