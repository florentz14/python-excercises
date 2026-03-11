# -------------------------------------------------
# File Name: 22_dict_to_series.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Converts a Python dictionary to a pandas Series.
# -------------------------------------------------

import pandas as pd

# Create a Python dictionary
dict_data = {"a": 100, "b": 200, "c": 300, "d": 400}
# Convert the dictionary to a pandas Series
series = pd.Series(dict_data)

# Print the original dictionary
print("Original Dictionary:")
# Print the pandas Series
print(dict_data)
print()
print("Pandas Series:")
print(series)
