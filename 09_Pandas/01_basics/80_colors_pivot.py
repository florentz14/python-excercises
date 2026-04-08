# -------------------------------------------------
# File Name: 80_colors_pivot.py
# Author: Florentino Báez
# Description: pivot_table — mean price by category and country (data_colors.csv).
# Data: 09_Pandas/data/data_colors.csv
# -------------------------------------------------

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "data" / "data_colors.csv"
df = pd.read_csv(csv_path, encoding="utf-8")

wide = pd.pivot_table(
    df,
    values="price",
    index="category",
    columns="country_origin",
    aggfunc="mean",
    fill_value=0,
)
print("Mean price: rows=category, cols=country_origin\n", wide.round(3))
