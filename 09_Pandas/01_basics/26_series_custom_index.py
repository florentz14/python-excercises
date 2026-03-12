# -------------------------------------------------
# File Name: 26_series_custom_index.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Creates a Series with a custom index.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a Series with a custom index
custom_index_series = pd.Series([5, 10, 15, 20, 25], index=["v", "w", "x", "y", "z"])
# print the Series
print("Series with custom index:")
print(custom_index_series)
