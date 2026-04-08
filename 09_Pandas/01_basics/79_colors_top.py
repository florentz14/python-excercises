# -------------------------------------------------
# File Name: 79_colors_top.py
# Author: Florentino Báez
# Description: nlargest() — top rows by a numeric column (data_colors.csv).
# Data: 09_Pandas/data/data_colors.csv
# -------------------------------------------------

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "data" / "data_colors.csv"
df = pd.read_csv(csv_path, encoding="utf-8")

top_price = pd.DataFrame(df.nlargest(5, "price"))
print("5 most expensive items:\n", top_price[["color", "object", "price", "category"]])
