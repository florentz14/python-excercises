# -------------------------------------------------
# File Name: 36_dict_to_series.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Converts a Python dictionary to a pandas Series.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a Python dictionary
dict_data = {"a": 100, "b": 200, "c": 300, "d": 400}
# convert the dictionary to a pandas Series
series = pd.Series(dict_data)

# print the original dictionary
print("Original Dictionary:")
# print the pandas Series
print(dict_data)
print()
print("pandas Series:")
print(series)
