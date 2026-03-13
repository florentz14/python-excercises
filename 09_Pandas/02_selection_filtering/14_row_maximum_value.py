# -------------------------------------------------
# File Name: 14_row_maximum_value.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Finds row indices of maximum values by column.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a dictionary with sample data
data = {"col1": [1, 2, 3, 4, 7], "col2": [4, 5, 6, 9, 5], "col3": [7, 8, 12, 1, 11]}

# create a DataFrame from the dictionary
df = pd.DataFrame(data)

# print the original DataFrame
print("Original DataFrame")
print(df)

# print row index with maximum value in each column
print("\nRow where col1 has maximum value:")
print(df["col1"].idxmax())
print("Row where col2 has maximum value:")
print(df["col2"].idxmax())
print("Row where col3 has maximum value:")
print(df["col3"].idxmax())
