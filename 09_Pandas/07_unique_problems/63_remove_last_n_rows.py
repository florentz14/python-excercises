# -------------------------------------------------
# File Name: 63_remove_last_n_rows.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 63 remove last n rows.
# -------------------------------------------------

"""Practice 63: Remove Last n Rows."""
import pandas as pd

data = {"col1": [1, 2, 3, 4, 7, 11], "col2": [4, 5, 6, 9, 5, 0], "col3": [7, 5, 8, 12, 1, 11]}
df_practice_63 = pd.DataFrame(data)
print("Original DataFrame")
print(df_practice_63)
df_practice_63 = df_practice_63.iloc[:-3]
print("\nAfter removing last 3 rows of the said DataFrame:")
print(df_practice_63)
