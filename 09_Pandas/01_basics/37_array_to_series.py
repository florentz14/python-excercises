# -------------------------------------------------
# File Name: 37_array_to_series.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Converting a NumPy array to a pandas Series.
# -------------------------------------------------

# import libraries
import numpy as np
import pandas as pd

# create a NumPy array
np_array = np.array([10, 20, 30, 40, 50])
# convert the NumPy array to a pandas Series
series = pd.Series(np_array)

# print the original NumPy array
print("original NumPy array:")
print(np_array)
print()
# print the pandas Series
print("pandas Series:")
print(series)
