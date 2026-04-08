# -------------------------------------------------
# File Name: 78_colors_filter.py
# Author: Florentino Báez
# Description: Boolean mask row selection (data_colors.csv).
# Data: 09_Pandas/data/data_colors.csv
# -------------------------------------------------

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "data" / "data_colors.csv"
df = pd.read_csv(csv_path, encoding="utf-8")

mask = (pd.Series(df["rating"]) >= 4.5) & (pd.Series(df["category"]) == "stationery")
filtered = pd.DataFrame(df.loc[mask, ["color", "object", "price", "rating"]])
print("stationery with rating >= 4.5:\n", filtered)
