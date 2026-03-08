# -------------------------------------------------
# File Name: 81_excel_operations.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Multiple sheets and read_excel operations.
# -------------------------------------------------

import pandas as pd
from pathlib import Path

df1 = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
df2 = pd.DataFrame({"x": [10, 20], "y": [30, 40]})

OUT = Path(__file__).parent.parent / "data" / "exports"
OUT.mkdir(parents=True, exist_ok=True)
xlsx_path = OUT / "multi_sheet.xlsx"

try:
    # Write multiple sheets
    with pd.ExcelWriter(xlsx_path, engine="openpyxl") as w:
        df1.to_excel(w, sheet_name="Data1", index=False)
        df2.to_excel(w, sheet_name="Data2", index=False)
    print("=== Write multiple sheets ===")
    print(f"Saved: {xlsx_path}")
    print()

    # Read specific sheet
    df_read = pd.read_excel(xlsx_path, sheet_name="Data1")
    print("=== read_excel(sheet_name='Data1') ===")
    print(df_read)
    print()

    # List all sheets
    xl = pd.ExcelFile(xlsx_path)
    print("=== Sheet names ===")
    print(xl.sheet_names)
    print()

    # Read all sheets to dict
    all_sheets = pd.read_excel(xlsx_path, sheet_name=None)
    print("=== Read all sheets ===")
    for name, d in all_sheets.items():
        print(f"{name}: {d.shape}")

except ImportError:
    print("pip install openpyxl")
    print("Skipped: openpyxl required for Excel")
