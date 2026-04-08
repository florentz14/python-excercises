# -------------------------------------------------
# File Name: 87_colors_del_col.py
# Author: Florentino Báez
# Description: Remove a column with del frame['column'] (drops it in place).
# Data: 09_Pandas/data/data_colors.csv (first 5 rows; color renamed to colors).
# -------------------------------------------------

from pathlib import Path

import pandas as pd

CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "data_colors.csv"
src = pd.read_csv(CSV_PATH, encoding="utf-8").head(5)
frame = pd.DataFrame(
    {"colors": src["color"], "object": src["object"], "price": src["price"]}
)

# Temporary column (e.g. computed); delete it when no longer needed
frame["new"] = 0
del frame["new"]

print(frame)
