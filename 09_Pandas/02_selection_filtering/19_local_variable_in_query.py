# -------------------------------------------------
# File Name: 19_local_variable_in_query.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Uses a local Python variable inside DataFrame query().
# -------------------------------------------------

# import libraries
import pandas as pd

# create a dictionary with sample data
data = {
    "W": [68, 75, 86, 80, 66],
    "X": [78, 85, 96, 80, 86],
    "Y": [84, 94, 89, 83, 86],
    "Z": [86, 97, 96, 72, 83],
}

# create a DataFrame from the dictionary
df = pd.DataFrame(data)

# print the original DataFrame
print("Original DataFrame")
print(df)

# get maximum W and use it inside query
max_w = df["W"].max()
result = df.query("W < @max_w")

# print filtered rows
print("\nValues which are less than maximum value of 'W' column")
print(result)
