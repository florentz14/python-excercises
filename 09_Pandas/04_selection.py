# -------------------------------------------------
# File Name: 04_selection.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Selects rows and columns using loc, iloc, and bracket notation.
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "name": ["Anna", "Louis", "Mary"],
    "age": [25, 30, 28],
    "balance": [100, 200, 150],
})

# Single column -> Series
print("Single column (Series):")
print(df["age"])

# Multiple columns -> DataFrame
print("\nMultiple columns:")
print(df[["name", "age"]])

# loc: by label (row/column name)
print("\nloc[0, 'name']:", df.loc[0, "name"])
print("loc[1:2, ['name','balance']]:")
print(df.loc[1:2, ["name", "balance"]])

# iloc: by numeric position
print("\niloc[0, 1]:", df.iloc[0, 1])
print("iloc[:, 0:2] (first 2 columns):")
print(df.iloc[:, 0:2])
