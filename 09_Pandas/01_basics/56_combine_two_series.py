# -------------------------------------------------
# File Name: 56_combine_two_series.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Combines two series into a DataFrame.
# -------------------------------------------------

# import libraries
import pandas as pd

# create two series
s1 = pd.Series([100, 200, "python", 300.12, 400])
s2 = pd.Series([10, 20, "php", 30.12, 40])

# print the series
print("Data Series:")
print(s1)
print(s2)

# combine the two series into a DataFrame
df = pd.concat([s1, s2], axis=1)

# print the DataFrame
print("\nNew DataFrame combining two series:")
print(df)
