# -------------------------------------------------
# File Name: 27_concat_pivot_basics.py
# Author: Florentino Baez
# Date: 09_Pandas
# Description: Concatenation, combine_first, stack, and unstack.
# -------------------------------------------------

import numpy as np
import pandas as pd

# 1. Concatenation (Series)
s1 = pd.Series([0, 1], index=["a", "b"])
s2 = pd.Series([2, 3, 4], index=["c", "d", "e"])
concatenated = pd.concat([s1, s2])

print("=== CONCAT SERIES ===")
print(concatenated)

# 2. Combine structures and fill nulls
df1 = pd.DataFrame({"a": [1, np.nan, 5, np.nan], "b": [np.nan, 2, np.nan, 6]})
df2 = pd.DataFrame({"a": [5, 4, np.nan, 3, 7], "b": [np.nan, 3, 4, 6, 8]})
combined = df1.combine_first(df2)

print("\n=== COMBINE FIRST ===")
print(combined)

# 3. Pivoting style: stack and unstack
stacked = df1.stack()
unstacked = stacked.unstack()

print("\n=== STACKED ===")
print(stacked)

print("\n=== UNSTACKED ===")
print(unstacked)
