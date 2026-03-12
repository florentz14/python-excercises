# -------------------------------------------------
# File Name: 53_drop_list_rows.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 36 drop list rows.
# -------------------------------------------------

"""Practice 36: Drop Rows from DataFrame."""
import pandas as pd

data = {"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]}

df_practice_36 = pd.DataFrame(data)
print("Original DataFrame")
print(df_practice_36)
df_practice_36 = df_practice_36.drop([2, 4])
print("\nNew DataFrame after removing 2nd & 4th rows:")
print(df_practice_36)
