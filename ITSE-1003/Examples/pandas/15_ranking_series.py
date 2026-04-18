# -------------------------------------------------
# File Name: 15_ranking_series.py
# Created: 2026-04-18
# Author: Florentino Báez
# Description: Ranking values in a Series with rank().
# -------------------------------------------------

import pandas as pd


ser = pd.Series([5, 0, 3, 8, 4], index=["red", "blue", "yellow", "white", "green"])

print("Original series:")
print(ser)
print()

print("ser.rank():")
print(ser.rank())
print()

print("ser.rank(method='first'):")
print(ser.rank(method="first"))
print()

print("ser.rank(ascending=False):")
print(ser.rank(ascending=False))
