# -------------------------------------------------
# File Name: 15_series_from_numpy.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Creates a pandas Series from a NumPy array.
# -------------------------------------------------

import numpy as np
import pandas as pd

# 2. Create a Series from a NumPy array
np_array = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
np_series = pd.Series(np_array)
print("Series from a NumPy array:")
print(np_series)
