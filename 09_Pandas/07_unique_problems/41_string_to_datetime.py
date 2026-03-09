# -------------------------------------------------
# File Name: 41_string_to_datetime.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 41 string to datetime.
# -------------------------------------------------

"""Practice 41: String to Datetime."""
import pandas as pd

s = pd.Series(["3/11/2000", "3/12/2000", "3/13/2000"])
print("String Date:")
print(s)
df_practice_41 = pd.DataFrame(pd.to_datetime(s))
print("\nOriginal DataFrame (string to datetime):")
print(df_practice_41)
