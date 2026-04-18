# -------------------------------------------------
# File Name: 30_read_csv_mycsv_01.py
# Created: 2026-04-18
# Author: Florentino Báez
# Description: read_csv example using colors_animals.csv.
# -------------------------------------------------

from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "colors_animals.csv"
csvframe = pd.read_csv(csv_path)

print("csvframe:")
print(csvframe)
