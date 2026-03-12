# -------------------------------------------------
# File Name: 67_add_prefix_suffix.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Adds prefix and suffix to DataFrame column names.
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

# print DataFrame with prefixed columns
print("\nAdd prefix:")
print(df.add_prefix("A_"))

# print DataFrame with suffixed columns
print("\nAdd suffix:")
print(df.add_suffix("_1"))
