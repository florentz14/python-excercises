# -------------------------------------------------
# File Name: 68_reverse_order.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 65 reverse order.
# -------------------------------------------------

"""Practice 65: Reverse Order of DataFrame (Rows, Columns)."""
import pandas as pd

data = {"W": [68, 75, 86, 80, 66], "X": [78, 85, 96, 80, 86], "Y": [84, 94, 89, 83, 86], "Z": [86, 97, 96, 72, 83]}
df_practice_65 = pd.DataFrame(data)
print("Original DataFrame")
print(df_practice_65)
print("\nReverse column order:")
print(df_practice_65[df_practice_65.columns[::-1]])
print("\nReverse row order:")
print(df_practice_65.iloc[::-1])
print("\nReverse row order and reset index:")
print(df_practice_65.iloc[::-1].reset_index(drop=True))
