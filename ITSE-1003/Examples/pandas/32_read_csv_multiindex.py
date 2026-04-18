# -------------------------------------------------
# File Name: 32_read_csv_multiindex.py
# Created: 2026-04-18
# Author: Florentino Báez
# Description: read_csv building a MultiIndex from CSV.
# -------------------------------------------------

from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "color_status_items.csv"
multi_index_frame = pd.read_csv(csv_path, index_col=["color", "status"])

print("read_csv(..., index_col=['color', 'status']):")
print(multi_index_frame)
