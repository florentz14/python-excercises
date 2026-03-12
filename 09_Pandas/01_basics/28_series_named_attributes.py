# -------------------------------------------------
# File Name: 28_series_named_attributes.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Creating a named Series and displaying key Series attributes.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a Series with a name and display attributes
named_series = pd.Series(
    [100, 200, 300, 400, 500],
    index=["Jan", "Feb", "Mar", "Apr", "May"],
    name="Monthly Sales",
)
# print the Series
print("Named Series:")
print(named_series)
print()
# print the name of the Series
print(f"Name   : {named_series.name}")
# print the dtype of the Series
print(f"dtype  : {named_series.dtype}")
# print the shape of the Series
print(f"shape  : {named_series.shape}")
# print the size of the Series
print(f"size   : {named_series.size}")
# print the values of the Series
print(f"Values : {named_series.values}")
# print the index of the Series
print(f"Index  : {named_series.index.tolist()}")
