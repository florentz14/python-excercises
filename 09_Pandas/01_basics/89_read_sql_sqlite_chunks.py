# -------------------------------------------------
# File Name: 89_read_sql_sqlite_chunks.py
# Author: Florentino Báez
# Date: 11/04/2026
# Description: Read SQLite CLOSING_PRICES in chunks with read_sql and concat.
# -------------------------------------------------

import sqlite3

import pandas as pd

conn = None
try:
    conn = sqlite3.connect("sample.db")
    SQL = "SELECT * FROM CLOSING_PRICES"
    dfiter = pd.read_sql(SQL, conn, chunksize=5)
    df_list = [df for df in dfiter]
    dfprices = pd.concat(df_list).reset_index(drop=True)
finally:
    if conn is not None:
        conn.close()
