# -------------------------------------------------
# File Name: 60_last_n_records.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 60 last n records.
# -------------------------------------------------

"""Practice 60: Get Last n Records."""
import pandas as pd

data = {"col1": [1, 2, 3, 4, 7, 11], "col2": [4, 5, 6, 9, 5, 0], "col3": [7, 5, 8, 12, 1, 11]}
df_practice_60 = pd.DataFrame(data)
print("Original DataFrame")
print(df_practice_60)
print("\nLast 3 rows of the said DataFrame:")
print(df_practice_60.tail(3))
