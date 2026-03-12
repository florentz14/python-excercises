# -------------------------------------------------
# File Name: 21_clean_object_column_regex.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 76 clean object column regex.
# -------------------------------------------------

"""Practice 76: Clean Object Column with Regex."""
import pandas as pd
import re

data = {"agent": ["a001", "a002", "a003", "a003", "a004"], "purchase": [4500, 7500, "$3000.25", "$1250.35", "9000.00"]}
df_practice_76 = pd.DataFrame(data)
print("Original dataframe:")
print(df_practice_76)
print("Data Types:")
print(df_practice_76["purchase"].apply(type))
df_practice_76["purchase"] = df_practice_76["purchase"].replace(r"[\$,]", "", regex=True).astype(float)
print("New Data Types:")
print(df_practice_76["purchase"].apply(type))
