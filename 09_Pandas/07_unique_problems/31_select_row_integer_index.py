# -------------------------------------------------
# File Name: 31_select_row_integer_index.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 31 select row integer index.
# -------------------------------------------------

"""Practice 31: Select Row by Integer Index."""
import pandas as pd

df_practice_31 = pd.DataFrame({"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]})
print("Original DataFrame")
print(df_practice_31)
print("\nIndex-2: Details")
print(df_practice_31.iloc[[2]])
