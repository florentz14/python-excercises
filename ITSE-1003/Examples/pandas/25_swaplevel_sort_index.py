# -------------------------------------------------
# File Name: 25_swaplevel_sort_index.py
# Created: 2026-04-18
# Author: Florentino Báez
# Description: swaplevel and sort_index on MultiIndex.
# -------------------------------------------------

import pandas as pd


ser = pd.Series(
    [10, 20, 30, 40],
    index=[
        ["A", "A", "B", "B"],
        ["one", "two", "one", "two"],
    ],
)

print("Original MultiIndex Series:")
print(ser)
print()

print("swaplevel():")
print(ser.swaplevel())
print()

print("swaplevel().sort_index():")
print(ser.swaplevel().sort_index())
