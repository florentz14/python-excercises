# -------------------------------------------------
# File Name: 23_rename_columns.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 23 rename columns.
# -------------------------------------------------

"""Practice 23: Renaming DataFrame Columns."""
import pandas as pd

df_practice_23 = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6], "col3": [7, 8, 9]})
print("Original DataFrame")
print(df_practice_23)

df_practice_23 = df_practice_23.rename(columns={"col1": "Column1", "col2": "Column2", "col3": "Column3"})
print("\nNew DataFrame after renaming columns:")
print(df_practice_23)
