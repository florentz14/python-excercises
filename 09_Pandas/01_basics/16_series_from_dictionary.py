# -------------------------------------------------
# File Name: 16_series_from_dictionary.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Creates a pandas Series from a Python dictionary.
# -------------------------------------------------

import pandas as pd

# 3. Create a Series from a dictionary
dict_data = {"a": 100, "b": 200, "c": 300, "d": 400}
dict_series = pd.Series(dict_data)
print("Series from a dictionary:")
print(dict_series)
