# -------------------------------------------------
# File Name: 61_topmost_n_per_group.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 61 topmost n per group.
# -------------------------------------------------

"""Practice 61: Get Topmost n Records Within Each Group."""
import pandas as pd

data = {"col1": [1, 2, 3, 4, 7, 11], "col2": [4, 5, 6, 9, 5, 0], "col3": [7, 5, 8, 12, 1, 11]}
df_practice_61 = pd.DataFrame(data)
print("Original DataFrame")
print(df_practice_61)
print("\ntopmost n records within each group of a DataFrame:")
for col in df_practice_61.columns:
    print(df_practice_61.nlargest(3, col))
    print()
