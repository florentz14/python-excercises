# -------------------------------------------------
# File Name: 17_series_custom_index.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Creates a pandas Series with a custom index.
# -------------------------------------------------

import pandas as pd

# 4. Create a Series with a custom index
custom_index_series = pd.Series([5, 10, 15, 20, 25], index=["v", "w", "x", "y", "z"])
print("Series with custom index:")
print(custom_index_series)
