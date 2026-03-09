# -------------------------------------------------
# File Name: 22_dict_to_series.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Converts a Python dictionary to a pandas Series.
# -------------------------------------------------

import pandas as pd

dict_data = {"a": 100, "b": 200, "c": 300, "d": 400}
series = pd.Series(dict_data)

print("Original Dictionary:")
print(dict_data)
print()
print("Pandas Series:")
print(series)
