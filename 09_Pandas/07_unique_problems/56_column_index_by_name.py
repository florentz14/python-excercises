# -------------------------------------------------
# File Name: 56_column_index_by_name.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 56 column index by name.
# -------------------------------------------------

"""Practice 56: Get Column Index by Column Name."""
import pandas as pd

data = {"col1": [1, 2, 3, 4, 7], "col2": [4, 5, 6, 9, 5], "col3": [7, 8, 12, 1, 11]}
df_practice_56 = pd.DataFrame(data)
print("Original DataFrame")
print(df_practice_56)
idx = df_practice_56.columns.get_loc("col2")
print(f"\nIndex of 'col2'")
print(idx)
