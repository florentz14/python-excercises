# -------------------------------------------------
# File Name: 19_to_numeric.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Convert object columns to numeric
# -------------------------------------------------

# import libraries
import pandas as pd

# create a Series with the data
s = pd.Series(["1", "2", "invalid", "4"])
# print the Series with errors='coerce'
print("to_numeric with errors='coerce':")
print(pd.to_numeric(s, errors="coerce"))
