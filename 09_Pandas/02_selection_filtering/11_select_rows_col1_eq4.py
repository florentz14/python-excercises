# -------------------------------------------------
# File Name: 11_select_rows_col1_eq4.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 24 select rows col1 eq4.
# -------------------------------------------------

"""Practice 24: Selecting Rows Based on Column Values."""
import pandas as pd

df_practice_24 = pd.DataFrame({"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]})
print("Original DataFrame")
print(df_practice_24)
print("\nRows for col1 value == 4")
print(df_practice_24[df_practice_24["col1"] == 4])
