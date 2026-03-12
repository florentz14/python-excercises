# -------------------------------------------------
# File Name: 16_value_counts.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Frequency counts and percentages
# -------------------------------------------------

# import libraries
import pandas as pd

# create a DataFrame with the color data
df = pd.DataFrame({"color": ["red", "blue", "red", "green", "blue", "red"]})
# print the counts of the color column
print("Counts:")
# print the counts of the color column with normalize=True (percentages)
print(df["color"].value_counts())
# print the counts of the color column with normalize=True (percentages)
print(df["color"].value_counts(normalize=True))
# print the counts of the color column with dropna=False
print(df["color"].value_counts(dropna=False))
