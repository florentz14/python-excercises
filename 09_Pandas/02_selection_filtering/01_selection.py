# -------------------------------------------------
# File Name: 01_selection.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Selects rows and columns using loc, iloc, and bracket notation.
# -------------------------------------------------

# import libraries
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    "name": ["Anna", "Louis", "Mary"],
    "age": [25, 30, 28],
    "balance": [100, 200, 150],
})

# Print the DataFrame
print("=== ORIGINAL DATAFRAME ===")
print(df)

# Single column -> Series
print("\n=== SINGLE COLUMN (SERIES) ===")
print("Single column (Series):")
print(df["age"])

# Multiple columns -> DataFrame
print("\n=== MULTIPLE COLUMNS (DATAFRAME) ===")
print("Multiple columns:")
print(df[["name", "age"]])

# loc: by label (row/column name)
print("\n=== LOC (BY LABEL) ===")
print("\nloc[0, 'name']:", df.loc[0, "name"])
print("loc[1:2, ['name','balance']]:")
print(df.loc[1:2, ["name", "balance"]])

# iloc: by numeric position
print("\niloc[0, 1]:", df.iloc[0, 1])
print("iloc[:, 0:2] (first 2 columns):")
print(df.iloc[:, 0:2])
