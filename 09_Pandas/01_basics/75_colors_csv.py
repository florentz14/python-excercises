# -------------------------------------------------
# File Name: 75_colors_csv.py
# Author: Florentino Báez
# Date: 4/8/2026
# Description: Read data_colors.csv and one basic groupby aggregation.
# Data: 09_Pandas/data/data_colors.csv
# -------------------------------------------------

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "data" / "data_colors.csv"
df = pd.read_csv(csv_path, encoding="utf-8")

print("First rows:\n", df.head())
print("\nAverage price by category (groupby + mean):")
avg_by_cat = pd.DataFrame(df.groupby("category", as_index=False).agg(avg_price=("price", "mean")))
print(avg_by_cat)
