# -------------------------------------------------
# File Name: 11_sorting_series_index.py
# Created: 2026-04-18
# Author: Florentino Báez
# Description: Sort a Series by index.
# -------------------------------------------------

import pandas as pd


ser = pd.Series([5, 0, 3, 8, 4], index=["red", "blue", "yellow", "white", "green"])

print("Original series:")
print(ser)
print()

print("ser.sort_index():")
print(ser.sort_index())
print()

print("ser.sort_index(ascending=False):")
print(ser.sort_index(ascending=False))
