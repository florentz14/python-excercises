# -------------------------------------------------
# File Name: 68_reverse_order.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Reverses DataFrame row and column order.
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

# reverse and print column order
print("\nReverse column order:")
print(df[df.columns[::-1]])

# reverse and print row order
print("\nReverse row order:")
print(df.iloc[::-1])

# reverse rows, reset index, and print result
print("\nReverse row order and reset index:")
print(df.iloc[::-1].reset_index(drop=True))
