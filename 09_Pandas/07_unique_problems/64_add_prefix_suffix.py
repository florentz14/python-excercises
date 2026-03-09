# -------------------------------------------------
# File Name: 64_add_prefix_suffix.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 64 add prefix suffix.
# -------------------------------------------------

"""Practice 64: Add Prefix or Suffix to All Columns."""
import pandas as pd

data = {"W": [68, 75, 86, 80, 66], "X": [78, 85, 96, 80, 86], "Y": [84, 94, 89, 83, 86], "Z": [86, 97, 96, 72, 83]}
df_practice_64 = pd.DataFrame(data)
print("Original DataFrame")
print(df_practice_64)
print("\nAdd prefix:")
print(df_practice_64.add_prefix("A_"))
print("\nAdd suffix:")
print(df_practice_64.add_suffix("_1"))
