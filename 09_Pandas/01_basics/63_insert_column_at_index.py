# -------------------------------------------------
# File Name: 63_insert_column_at_index.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Inserts a column at a specific index in a DataFrame.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a DataFrame with two columns
df = pd.DataFrame({"col2": [4, 5, 6, 9, 5], "col3": [7, 8, 12, 1, 11]})

# print the original DataFrame
print("Original DataFrame")
print(df)

# create a Series with the values for the new column
col1 = pd.Series([1, 2, 3, 4, 7])

# insert the new column at index 0
df.insert(0, "col1", col1)

# print the new DataFrame
print("\nNew DataFrame")
print(df)
