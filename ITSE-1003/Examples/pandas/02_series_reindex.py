# -------------------------------------------------
# File Name: 02_series_reindex.py
# Created: 2026-04-18
# Author: Florentino Báez
# Description: Reindex a pandas Series with a new index.
# -------------------------------------------------

import pandas as pd

ser = pd.Series([2, 5, 7, 4], index=["one", "two", "three", "four"])
ser = ser.reindex(["three", "four", "five", "one"])

print(ser)
