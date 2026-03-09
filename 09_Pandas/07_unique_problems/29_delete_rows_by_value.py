# -------------------------------------------------
# File Name: 29_delete_rows_by_value.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 29 delete rows by value.
# -------------------------------------------------

"""Practice 29: Delete Rows by Column Value."""
import pandas as pd

df_practice_29 = pd.DataFrame({"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]})
print("Original DataFrame")
print(df_practice_29)
df_practice_29 = df_practice_29[df_practice_29["col2"] != 5]
print("\nNew DataFrame")
print(df_practice_29)
