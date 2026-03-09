# -------------------------------------------------
# File Name: 58_select_all_except_one.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 58 select all except one.
# -------------------------------------------------

"""Practice 58: Select All Except One Column."""
import pandas as pd

data = {"col1": [1, 2, 3, 4, 7], "col2": [4, 5, 6, 9, 5], "col3": [7, 8, 12, 1, 11]}
df_practice_58 = pd.DataFrame(data)
print("Original DataFrame")
print(df_practice_58)
print("\nAll columns except 'col3':")
print(df_practice_58.drop(columns=["col3"]))
