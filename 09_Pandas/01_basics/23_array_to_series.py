# -------------------------------------------------
# File Name: 23_array_to_series.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Converts a NumPy array to a pandas Series.
# -------------------------------------------------

import numpy as np
import pandas as pd

# Create a NumPy array
np_array = np.array([10, 20, 30, 40, 50])
# Convert the NumPy array to a pandas Series
series = pd.Series(np_array)

# Print the original NumPy array
print("Original NumPy Array:")
print(np_array)
print()
# Print the pandas Series
print("Pandas Series:")
print(series)
