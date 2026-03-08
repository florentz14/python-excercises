# -------------------------------------------------
# File Name: 89_data_quality_report.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Automatic data quality checks and report generation.
# -------------------------------------------------

from pathlib import Path

import pandas as pd
import numpy as np

DATA = Path(__file__).parent / "data"
df = pd.read_csv(DATA / "store_sales.csv")

print("=" * 60)
print("DATA QUALITY REPORT")
print("=" * 60)
print()

# 1. Shape
print("=== SHAPE ===")
print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
print()

# 2. Nulls
print("=== NULL COUNTS ===")
nulls = df.isna().sum()
print(nulls[nulls > 0] if nulls.any() else "No nulls")
print()

# 3. Duplicates
dup_rows = df.duplicated().sum()
print("=== DUPLICATES ===")
print(f"Duplicate rows: {dup_rows}")
print()

# 4. Dtypes
print("=== DTYPES ===")
print(df.dtypes)
print()

# 5. Numeric stats
print("=== NUMERIC SUMMARY ===")
print(df.select_dtypes(include=[np.number]).describe())
print()

# 6. Value counts for object columns
obj_cols = df.select_dtypes(include="object").columns
if len(obj_cols) > 0:
    print("=== UNIQUE COUNTS (object cols) ===")
    for c in obj_cols:
        print(f"{c}: {df[c].nunique()} unique")
print()

# 7. Potential issues
print("=== POTENTIAL ISSUES ===")
for col in df.select_dtypes(include=[np.number]).columns:
    zeros = (df[col] == 0).sum()
    neg = (df[col] < 0).sum()
    if zeros > 0:
        print(f"  {col}: {zeros} zeros")
    if neg > 0:
        print(f"  {col}: {neg} negative values")
