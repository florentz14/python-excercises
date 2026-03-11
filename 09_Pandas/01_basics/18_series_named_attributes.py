# -------------------------------------------------
# File Name: 18_series_named_attributes.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Creates a named Series and displays key Series attributes.
# -------------------------------------------------

import pandas as pd

# Create a Series with a name and display attributes
named_series = pd.Series(
    [100, 200, 300, 400, 500],
    index=["Jan", "Feb", "Mar", "Apr", "May"],
    name="Monthly Sales",
)
# Print the Series
print("Named Series:")
print(named_series)
print()
# Print the name of the Series
print(f"Name   : {named_series.name}")
# Print the dtype of the Series
print(f"dtype  : {named_series.dtype}")
# Print the shape of the Series
print(f"shape  : {named_series.shape}")
# Print the size of the Series
print(f"size   : {named_series.size}")
# Print the values of the Series
print(f"Values : {named_series.values}")
# Print the index of the Series
print(f"Index  : {named_series.index.tolist()}")
