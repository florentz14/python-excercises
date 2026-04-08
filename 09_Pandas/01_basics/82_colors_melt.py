# -------------------------------------------------
# File Name: 82_colors_melt.py
# Author: Florentino Báez
# Description: melt() — wide metrics to long rows (data_colors.csv).
# Data: 09_Pandas/data/data_colors.csv
# -------------------------------------------------

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "data" / "data_colors.csv"
df = pd.read_csv(csv_path, encoding="utf-8")

long_df = pd.DataFrame(
    df.melt(
        id_vars=["color", "object", "category"],
        value_vars=["price", "stock", "rating"],
        var_name="metric",
        value_name="value",
    )
)
print("Long format (first 12 rows):\n", long_df.head(12))
