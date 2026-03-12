# -------------------------------------------------
# File Name: 42_add_one_row.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 26 add one row.
# -------------------------------------------------

"""Practice 26: Add One Row to a DataFrame."""
import pandas as pd

df_practice_26 = pd.DataFrame({"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]})
print("Original DataFrame")
print(df_practice_26)
df_practice_26.loc[len(df_practice_26)] = [10, 11, 12]
print("\nAfter add one row:")
print(df_practice_26)
