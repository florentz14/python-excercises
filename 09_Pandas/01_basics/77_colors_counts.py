# -------------------------------------------------
# File Name: 77_colors_counts.py
# Author: Florentino Báez
# Description: value_counts() on categorical columns (data_colors.csv).
# Data: 09_Pandas/data/data_colors.csv
# -------------------------------------------------

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "data" / "data_colors.csv"
df = pd.read_csv(csv_path, encoding="utf-8")

cat_counts = pd.Series(df["category"]).value_counts()
color_counts = pd.Series(df["color"]).value_counts()

print("Rows per category:\n", cat_counts)
print("\nRows per color (top 5):\n", color_counts.head())
