"""
Pandas + SQLite3: leer consultas SQL a DataFrame y escribir DataFrames a tablas.

Requisitos: pandas (sqlite3 viene con Python).

Desde la raíz del repo:
    python ITSE-1003/Examples/databases/01_pandas_sqlite_read_write.py
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT.parent / "data" / "pandas_sqlite_demo.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)


def main() -> None:
    # Quitar DB anterior para que cada ejecución sea reproducible (opcional en proyectos reales).
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(DB_PATH)

    try:
        # 1) Tabla con id autoincremental (INTEGER PRIMARY KEY en SQLite).
        #    Definimos el esquema con SQL; pandas solo inserta sku, name, price.
        conn.execute(
            """
            CREATE TABLE products (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                sku   TEXT    NOT NULL,
                name  TEXT    NOT NULL,
                price REAL    NOT NULL
            )
            """
        )
        conn.commit()

        products = pd.DataFrame(
            {
                "sku": ["A1", "A2", "B1"],
                "name": ["Mouse", "Keyboard", "USB cable"],
                "price": [12.5, 45.0, 5.99],
            }
        )
        products.to_sql("products", conn, if_exists="append", index=False)

        # 2) Leer toda la tabla a un DataFrame.
        df_all = pd.read_sql_query("SELECT * FROM products", conn)
        print("--- SELECT * FROM products ---")
        print(df_all, "\n")

        # 3) Consulta con filtro (parámetros: usa ? con sqlite3).
        min_price = 15.0
        df_filtered = pd.read_sql_query(
            "SELECT id, sku, name FROM products WHERE price >= ? ORDER BY price",
            conn,
            params=[min_price],
        )
        print(f"--- Productos con price >= {min_price} ---")
        print(df_filtered, "\n")

        # 4) Añadir filas con otro DataFrame (append) y volver a leer.
        more = pd.DataFrame(
            {"sku": ["C9"], "name": ["Webcam"], "price": [79.0]}
        )
        more.to_sql("products", conn, if_exists="append", index=False)
        df_after = pd.read_sql_query("SELECT * FROM products ORDER BY id", conn)
        print("--- Tras append de una fila ---")
        print(df_after, "\n")

        print(f"Base de datos guardada en: {DB_PATH}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
