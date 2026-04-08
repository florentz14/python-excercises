# -------------------------------------------------
# File Name: 88_colors_frame_lt.py
# Author: Florentino Báez
# Description: Boolean mask on the whole DataFrame — keeps values where True, else NaN.
# Uses the same 4x4 grid as 85_colors_frame_np.py (from data_colors.csv, weight_g).
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

frame = pd.DataFrame(block, index=colors, columns=objects)
print(frame[frame < 12])
