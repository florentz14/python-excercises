# -------------------------------------------------
# File Name: 83_colors_merge.py
# Author: Florentino Báez
# Description: merge() — join items with category metadata (lookup CSV).
# Data: 09_Pandas/data/data_colors.csv, data_colors_meta.csv
# -------------------------------------------------

from pathlib import Path

import pandas as pd

root = Path(__file__).resolve().parent.parent
df = pd.read_csv(root / "data" / "data_colors.csv", encoding="utf-8")
meta = pd.read_csv(root / "data" / "data_colors_meta.csv", encoding="utf-8")

merged = pd.DataFrame(pd.merge(df, meta, on="category", how="left"))
tax = pd.Series(merged["tax_pct"])
price = pd.Series(merged["price"])
merged["price_after_tax"] = (price * (1 + tax / 100)).round(3)

print(merged[["object", "category", "price", "tax_pct", "warehouse", "price_after_tax"]].head(10))
