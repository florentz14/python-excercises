# -------------------------------------------------
# File Name: 58_column_to_list.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Converts a column in a DataFrame to a list.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a dictionary of data
data = {"col1": [1, 2, 3], "col2": [4, 5, 6], "col3": [7, 8, 9]}

# create a DataFrame from the dictionary
df = pd.DataFrame(data)

# print the original DataFrame
print("Original DataFrame")
print(df)

# print the second column as a list
print("\nCol2 of the DataFrame to list:")
print(df["col2"].tolist())
