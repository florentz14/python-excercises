# -------------------------------------------------
# File Name: 80_export_files.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Exports to CSV, JSON, Excel, Parquet formats.
# -------------------------------------------------

import pandas as pd
from pathlib import Path

df = pd.DataFrame({
    "name": ["Anna", "Bob", "Carol"],
    "score": [85, 90, 78],
    "active": [True, True, False],
})

OUT = Path(__file__).parent.parent / "data" / "exports"
OUT.mkdir(parents=True, exist_ok=True)

# CSV
csv_path = OUT / "export_sample.csv"
df.to_csv(csv_path, index=False, encoding="utf-8")
print("=== to_csv (index=False) ===")
print(f"Saved: {csv_path}")
print()

# CSV with custom separator
df.to_csv(OUT / "export_semicolon.csv", index=False, sep=";")
print("=== to_csv (sep=';') ===")
print("Saved: export_semicolon.csv")
print()

# JSON
json_path = OUT / "export_sample.json"
df.to_json(json_path, orient="records", indent=2)
print("=== to_json (orient='records') ===")
print(f"Saved: {json_path}")
print()

# Excel (requires openpyxl)
try:
    xlsx_path = OUT / "export_sample.xlsx"
    df.to_excel(xlsx_path, index=False, sheet_name="Sheet1")
    print("=== to_excel ===")
    print(f"Saved: {xlsx_path}")
except ImportError:
    print("=== to_excel (pip install openpyxl) ===")
    print("Skipped: openpyxl not installed")
print()

# Parquet (requires pyarrow)
try:
    pq_path = OUT / "export_sample.parquet"
    df.to_parquet(pq_path, index=False)
    print("=== to_parquet ===")
    print(f"Saved: {pq_path}")
except ImportError:
    print("=== to_parquet (pip install pyarrow) ===")
    print("Skipped: pyarrow not installed")
