# -------------------------------------------------
# File Name: 81_colors_assign.py
# Author: Florentino Báez
# Description: assign() — add derived columns without mutating the original DataFrame.
# Data: 09_Pandas/data/data_colors.csv
# -------------------------------------------------

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "data" / "data_colors.csv"
df = pd.read_csv(csv_path, encoding="utf-8")

price = pd.Series(df["price"])
stock = pd.Series(df["stock"])
rating = pd.Series(df["rating"])

enriched = pd.DataFrame(
    df.assign(
        stock_value=price * stock,
        rating_weighted=price * rating,
    )
)
print(enriched[["object", "category", "price", "stock", "stock_value", "rating_weighted"]].head(8))
