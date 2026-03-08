# -------------------------------------------------
# File Name: 02_read_csv.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Reads a CSV file into a DataFrame and shows basic export options.
# -------------------------------------------------

import pandas as pd
from pathlib import Path

# Path to CSV (data is in 09_Pandas/data/)
csv_path = Path(__file__).parent.parent / "data" / "data.csv"

# Read CSV
df = pd.read_csv(csv_path, encoding="utf-8")
# Export: df.to_csv(Path(__file__).parent / "output.csv", index=False)
print("Loaded DataFrame:")
print(df.head())
print("\nColumns:", df.columns.tolist())
print("Shape:", df.shape)

