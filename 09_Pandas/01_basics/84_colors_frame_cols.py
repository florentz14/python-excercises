# -------------------------------------------------
# File Name: 84_colors_frame_cols.py
# Author: Florentino Báez
# Description: DataFrame from dict with columns= (subset and column order).
# Data: 09_Pandas/data/data_colors.csv (first 5 rows).
# -------------------------------------------------

from pathlib import Path

import pandas as pd

CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "data_colors.csv"
src = pd.read_csv(CSV_PATH, encoding="utf-8").head(5)

data = {
    "object": src["object"].tolist(),
    "price": src["price"].tolist(),
    "color": src["color"].tolist(),
}

frame2 = pd.DataFrame(data, columns=["object", "price"])
print(frame2)
