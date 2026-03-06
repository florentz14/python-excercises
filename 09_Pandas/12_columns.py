# ------------------------------------------------------------
# File: 12_columns.py
# Purpose: Select and create columns.
# Description: df["col"] returns a Series; df[["c1","c2"]] returns DataFrame.
#              Assign to df["new"] to create a computed column.
# ------------------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "name": ["Anna", "Louis", "Mary"],
    "age": [25, 30, 28],
    "balance": [100, 200, 150],
})

# Select single column (Series)
print("Column 'age':\n", df["age"])

# Select multiple columns (DataFrame)
print("\nColumns name and age:\n", df[["name", "age"]])

# Create new column
df["double_balance"] = df["balance"] * 2
print("\nDataFrame with new column:\n", df)
