# -------------------------------------------------
# File Name: 40_change_column_order.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Changing the order of the columns of a DataFrame.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a DataFrame with the exam data
df_change_column_order = pd.DataFrame({"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]})
# print the original DataFrame
print("original DataFrame")
print(df_change_column_order)
df_change_column_order = df_change_column_order[["col3", "col2", "col1"]]
print("\nafter altering col1 and col3")
# print the new DataFrame after altering col1 and col3
print(df_change_column_order)
