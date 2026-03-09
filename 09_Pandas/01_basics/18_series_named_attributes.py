# -------------------------------------------------
# File Name: 18_series_named_attributes.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Creates a named Series and displays key Series attributes.
# -------------------------------------------------

import pandas as pd

# 5. Create a Series with a name and display attributes
named_series = pd.Series(
    [100, 200, 300, 400, 500],
    index=["Jan", "Feb", "Mar", "Apr", "May"],
    name="Monthly Sales",
)
print("Named Series:")
print(named_series)
print()
print(f"Name   : {named_series.name}")
print(f"dtype  : {named_series.dtype}")
print(f"shape  : {named_series.shape}")
print(f"size   : {named_series.size}")
print(f"Values : {named_series.values}")
print(f"Index  : {named_series.index.tolist()}")
