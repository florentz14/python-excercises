# -------------------------------------------------
# File Name: 24_series_from_dictionary.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Creates a Series from a Python dictionary.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a Series from a dictionary
dict_data = {"a": 100, "b": 200, "c": 300, "d": 400}
dict_series = pd.Series(dict_data)
# print the Series
print("Series from a dictionary:")
print(dict_series)

# create a Series with repeated index labels
serd = pd.Series([1, 0, 2, 1, 2, 3], index=["white", "white", "blue", "green", "green", "yellow"])
print("\nSeries with repeated index labels:")
print(serd)
