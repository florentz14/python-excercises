# -------------------------------------------------
# File Name: 17_select_all_except_one.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Selects all columns except one specified column.
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

# print all columns except 'col3'
print("\nAll columns except 'col3':")
print(df.drop(columns=["col3"]))
