# -------------------------------------------------
# File Name: 47_get_row_value.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 47 get row value.
# -------------------------------------------------

"""Practice 47: Get Row Value."""
import pandas as pd

data = {"col1": [1, 2, 3, 4, 7], "col2": [4, 5, 6, 9, 5], "col3": [7, 8, 12, 1, 11]}
df_practice_47 = pd.DataFrame(data)
print("Original DataFrame")
print(df_practice_47)
print("\nValue of Row 0")
print(df_practice_47.iloc[0])
print("\nValue of Row4")
print(df_practice_47.iloc[3])
