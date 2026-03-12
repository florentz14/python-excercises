# -------------------------------------------------
# File Name: 44_concat_pivot_basics.py
# Author: Florentino Baez
# Date: 12/03/2026
# Description: Concatenation, combine_first, stack, and unstack.
# -------------------------------------------------

# Import numpy and pandas libraries
import numpy as np
import pandas as pd

# Create a first Series
s1 = pd.Series([0, 1], index=["a", "b"])
s2 = pd.Series([2, 3, 4], index=["c", "d", "e"])
concatenated = pd.concat([s1, s2])

print("=== CONCAT SERIES ===")
print(concatenated)

# Create a first DataFrame
df1 = pd.DataFrame({"a": [1, np.nan, 5, np.nan], "b": [np.nan, 2, np.nan, 6]})

# Create a second DataFrame
df2 = pd.DataFrame({"a": [5, 4, np.nan, 3, 7], "b": [np.nan, 3, 4, 6, 8]})

# Combine the first and second DataFrame
combined = df1.combine_first(df2)

print("\n=== COMBINE FIRST ===")
print(combined)

# Stack the first DataFrame
stacked = df1.stack()

# Unstack the stacked DataFrame
unstacked = stacked.unstack()

# Print the stacked DataFrame
print("\n=== STACKED ===")
print(stacked)

# Print the unstacked DataFrame
print("\n=== UNSTACKED ===")
print(unstacked)
