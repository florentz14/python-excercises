# -------------------------------------------------
# File Name: 85_colors_frame_np.py
# Author: Florentino Báez
# Description: 4x4 DataFrame from data_colors.csv (mean weight_g by color x object).
# Index/column order matches the classic example: red, blue, yellow, white x ball..paper.
# -------------------------------------------------

from pathlib import Path

import pandas as pd

CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "data_colors.csv"
df = pd.read_csv(CSV_PATH, encoding="utf-8")

row_order = ["red", "blue", "yellow", "white"]
col_order = ["ball", "pen", "pencil", "paper"]
colors = [c for c in row_order if c in set(df["color"])]
objects = [o for o in col_order if o in set(df["object"])]

block: list[list[float]] = []
for c in colors:
    row: list[float] = []
    for o in objects:
        m = df.loc[(df["color"] == c) & (df["object"] == o), "weight_g"]
        row.append(float(m.mean()) if len(m) else float("nan"))
    block.append(row)

frame3 = pd.DataFrame(block, index=colors, columns=objects)
print(frame3)
