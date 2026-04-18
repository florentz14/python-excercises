# -------------------------------------------------
# File Name: 01_series_basic.py
# Created: 2026-04-18
# Author: Florentino Báez
# Description: Create a basic pandas Series with index.
# -------------------------------------------------

import pandas as pd

ser = pd.Series([2, 5, 7, 4], index=["one", "two", "three", "four"])

print("Basic pandas Series:")
print(ser)
