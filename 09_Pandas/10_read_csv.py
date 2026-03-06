# ------------------------------------------------------------
# File: 10_read_csv.py
# Purpose: Read a CSV file into a DataFrame.
# Description: pd.read_csv() loads a CSV and returns a DataFrame.
#              Shows column names, shape, and first 5 rows with head().
# ------------------------------------------------------------

import pandas as pd
from pathlib import Path

# Path to data.csv in project root (one folder above 09_Pandas)
csv_path = Path(__file__).parent / "data" / "data.csv"

# Load CSV into DataFrame
df = pd.read_csv(csv_path, encoding="utf-8")
print(df)

print("\nColumns:", df.columns.tolist())
print("Dimensions:", df.shape)

print("\nFirst 5 rows:")
print(df.head())
