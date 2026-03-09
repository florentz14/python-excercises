# -------------------------------------------------
# File Name: 46_check_column_presence.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 46 check column presence.
# -------------------------------------------------

"""Practice 46: Check Column Presence."""
import pandas as pd

data = {"col1": [1, 2, 3, 4, 7], "col2": [4, 5, 6, 9, 5], "col3": [7, 8, 12, 1, 11]}
df_practice_46 = pd.DataFrame(data)
print("Original DataFrame")
print(df_practice_46)
for col in ["col4", "col1"]:
    if col in df_practice_46.columns:
        print(f"{col} is present in DataFrame.")
    else:
        print(f"{col} is not present in DataFrame.")
