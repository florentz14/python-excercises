# -------------------------------------------------
# File Name: 31_read_table_with_sep.py
# Created: 2026-04-18
# Author: Florentino Báez
# Description: read_table with explicit separator on sample CSV.
# -------------------------------------------------

from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "colors_animals.csv"
table_frame = pd.read_table(csv_path, sep=",")

print("read_table(..., sep=','):")
print(table_frame)
