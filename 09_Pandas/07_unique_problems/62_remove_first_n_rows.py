# -------------------------------------------------
# File Name: 62_remove_first_n_rows.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 62 remove first n rows.
# -------------------------------------------------

"""Practice 62: Remove First n Rows."""
import pandas as pd

data = {"col1": [1, 2, 3, 4, 7, 11], "col2": [4, 5, 6, 9, 5, 0], "col3": [7, 5, 8, 12, 1, 11]}
df_practice_62 = pd.DataFrame(data)
print("Original DataFrame")
print(df_practice_62)
df_practice_62 = df_practice_62.iloc[3:]
print("\nAfter removing first 3 rows of the said DataFrame:")
print(df_practice_62)
