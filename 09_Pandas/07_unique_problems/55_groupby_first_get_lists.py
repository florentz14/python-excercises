# -------------------------------------------------
# File Name: 55_groupby_first_get_lists.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 55 groupby first get lists.
# -------------------------------------------------

"""Practice 55: Group by First Column to Get Lists."""
import pandas as pd

data = {"col1": ["C1", "C1", "C2", "C2", "C2", "C3", "C2"], "col2": [1, 2, 3, 3, 4, 6, 5]}
df_practice_55 = pd.DataFrame(data)
print("Original DataFrame")
print(df_practice_55)
result = df_practice_55.groupby("col1")["col2"].apply(list)
print("\nGroup on the col1:")
print(result)
