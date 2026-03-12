# -------------------------------------------------
# File Name: 56_combine_two_series.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 39 combine two series.
# -------------------------------------------------

"""Practice 39: Combine Two Series."""
import pandas as pd

s1 = pd.Series([100, 200, "python", 300.12, 400])
s2 = pd.Series([10, 20, "php", 30.12, 40])
print("Data Series:")
print(s1)
print(s2)
df_practice_39 = pd.concat([s1, s2], axis=1)
print("\nNew DataFrame combining two series:")
print(df_practice_39)
