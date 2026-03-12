# -------------------------------------------------
# File Name: 38_rename_columns.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Renaming the columns of a DataFrame.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a DataFrame with the exam data
df_rename_columns = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6], "col3": [7, 8, 9]})
# print the original DataFrame
print("original DataFrame")
print(df_rename_columns)

# rename the columns of the DataFrame
df_rename_columns = df_rename_columns.rename(columns={"col1": "Column1", "col2": "Column2", "col3": "Column3"})
# print the new DataFrame after renaming columns
print("\nnew DataFrame after renaming columns:")
print(df_rename_columns)
