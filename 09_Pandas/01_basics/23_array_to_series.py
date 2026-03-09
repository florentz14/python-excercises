# -------------------------------------------------
# File Name: 23_array_to_series.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Converts a NumPy array to a pandas Series.
# -------------------------------------------------

import numpy as np
import pandas as pd

np_array = np.array([10, 20, 30, 40, 50])
series = pd.Series(np_array)

print("Original NumPy Array:")
print(np_array)
print()
print("Pandas Series:")
print(series)
