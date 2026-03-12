# -------------------------------------------------
# File Name: 65_column_index_by_name.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Gets the index of a DataFrame column by its name.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a dictionary with sample data
data = {
    "col1": [1, 2, 3, 4, 7],
    "col2": [4, 5, 6, 9, 5],
    "col3": [7, 8, 12, 1, 11],
}

# create a DataFrame from the dictionary
df = pd.DataFrame(data)

# print the original DataFrame
print("Original DataFrame")
print(df)

# get the index position of column 'col2'
idx = df.columns.get_loc("col2")

# print the index of the selected column
print("\nIndex of 'col2'")
print(idx)
