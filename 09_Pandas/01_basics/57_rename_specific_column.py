# -------------------------------------------------
# File Name: 57_rename_specific_column.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Renames a specific column in a DataFrame.
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

# rename the second column
df = df.rename(columns={"col2": "Column2"})

# print the new DataFrame
print("\nNew DataFrame after renaming second column:")
print(df)
