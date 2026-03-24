# -------------------------------------------------
# File Name: ITSE-1003/Examples/data_preview.py
# Author: Florentino Báez
# Date: 3/21/2026
# Description: Preview bundled CSVs and SQLite tables under data/ (stdlib only).
# -------------------------------------------------

from __future__ import annotations

import csv
import sqlite3
from pathlib import Path

from examples_paths import (
    DATA_DIR,
    EXAM_DATA_CSV,
    HOSPITAL_DATA_CSV,
    HOSPITAL_DATA_DIR,
    INVOICE_LINES_CSV,
    INVOICES_CSV,
    PEOPLE_CSV,
    SALES_DB,
    SCHOOL_DB,
    SALES_DATA_DIR,
    VEHICLES_CSV,
)


def _preview_csv(path: Path, label: str, max_rows: int = 4) -> None:
    print(f"\n--- {label}: {path.name} ---")
    if not path.is_file():
        print(f"  (missing: {path})")
        return
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = []
        for i, row in enumerate(reader):
            rows.append(row)
            if i >= max_rows:
                break
    if not rows:
        print("  (empty file)")
        return
    print(f"  columns: {rows[0]}")
    for row in rows[1:]:
        print(f"  {row}")


def _preview_sqlite(db_path: Path, *, missing_hint: str | None = None) -> None:
    print(f"\n--- SQLite: {db_path.name} ---")
    if not db_path.is_file():
        hint = missing_hint or "python data/build_school_db.py (school.db) o python sales/gestion_ventas.py (sales.db)"
        print(f"  (missing — {hint})")
        return
    conn = sqlite3.connect(db_path)
    try:
        tables = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        ).fetchall()
        print(f"  tables: {[t[0] for t in tables]}")
        for (name,) in tables:
            n = conn.execute(f'SELECT COUNT(*) FROM "{name}"').fetchone()[0]
            print(f"  {name}: {n} rows")
    finally:
        conn.close()


def main() -> None:
    print("Bundled data under:", DATA_DIR.resolve())
    print("Hospital (hospital_data.csv):", HOSPITAL_DATA_DIR.resolve())
    print("Ventas (facturas + sales.db):", SALES_DATA_DIR.resolve())
    _preview_csv(PEOPLE_CSV, "People")
    _preview_csv(EXAM_DATA_CSV, "Exam scores")
    _preview_csv(HOSPITAL_DATA_CSV, "Hospital demo")
    _preview_csv(VEHICLES_CSV, "Vehicles demo")
    _preview_csv(INVOICES_CSV, "Invoices (master)")
    _preview_csv(INVOICE_LINES_CSV, "Invoice lines (detail)")
    _preview_sqlite(SCHOOL_DB, missing_hint="python data/build_school_db.py")
    _preview_sqlite(
        SALES_DB,
        missing_hint="python sales/gestion_ventas.py (crea sales/data/sales.db)",
    )


if __name__ == "__main__":
    main()
