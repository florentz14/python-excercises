# -------------------------------------------------
# File Name: 66_count_columns.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 57 count columns.
# -------------------------------------------------

"""Practice 57: Count Number of Columns."""
import pandas as pd

data = {"col1": [1, 2, 3, 4, 7], "col2": [4, 5, 6, 9, 5], "col3": [7, 8, 12, 1, 11]}
df_practice_57 = pd.DataFrame(data)
print("Original DataFrame")
print(df_practice_57)
print(f"\nNumber of columns:")
print(len(df_practice_57.columns))
