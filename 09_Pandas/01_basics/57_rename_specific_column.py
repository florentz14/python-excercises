# -------------------------------------------------
# File Name: 57_rename_specific_column.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 42 rename specific column.
# -------------------------------------------------

"""Practice 42: Rename Specific Column."""
import pandas as pd

data = {"col1": [1, 2, 3], "col2": [4, 5, 6], "col3": [7, 8, 9]}
df_practice_42 = pd.DataFrame(data)
print("Original DataFrame")
print(df_practice_42)
df_practice_42 = df_practice_42.rename(columns={"col2": "Column2"})
print("\nNew DataFrame after renaming second column:")
print(df_practice_42)
