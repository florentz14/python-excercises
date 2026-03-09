# -------------------------------------------------
# File Name: 25_change_column_order.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 25 change column order.
# -------------------------------------------------

"""Practice 25: Changing the Order of DataFrame Columns."""
import pandas as pd

df_practice_25 = pd.DataFrame({"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]})
print("Original DataFrame")
print(df_practice_25)
df_practice_25 = df_practice_25[["col3", "col2", "col1"]]
print("\nAfter altering col1 and col3")
print(df_practice_25)
