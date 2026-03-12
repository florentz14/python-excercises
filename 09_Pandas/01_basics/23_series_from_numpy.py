# -------------------------------------------------
# File Name: 23_series_from_numpy.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Creates a Series from a NumPy array.
# -------------------------------------------------

# import libraries
import numpy as np
import pandas as pd

# create a Series from a NumPy array
np_array = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
np_series = pd.Series(np_array)
# print the Series
print("Series from a NumPy array:")
print(np_series)
