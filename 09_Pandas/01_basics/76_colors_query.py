# -------------------------------------------------
# File Name: 76_colors_query.py
# Author: Florentino Báez
# Description: Filter rows with DataFrame.query() on data_colors.csv.
# Data: 09_Pandas/data/data_colors.csv
# -------------------------------------------------

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "data" / "data_colors.csv"
df = pd.read_csv(csv_path, encoding="utf-8")

# String expression: multiple conditions (use column names as variables)
picked = pd.DataFrame(df.query("price > 1.2 and stock < 200"))
print("query: price > 1.2 and stock < 200\n", picked)
