# -------------------------------------------------
# File Name: 86_colors_frame_names.py
# Author: Florentino Báez
# Description: index.name and columns.name — labels for the index and column axis.
# Data: 09_Pandas/data/data_colors.csv (first 5 rows).
# -------------------------------------------------

from pathlib import Path

import pandas as pd

CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "data_colors.csv"
frame = pd.read_csv(CSV_PATH, encoding="utf-8").head(5)[["color", "object", "price"]]

frame.index.name = "id"
frame.columns.name = "item"

print(frame)
