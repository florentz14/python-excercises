# -------------------------------------------------
# File Name: 66_count_columns.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Counts the number of columns in a DataFrame.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a dictionary with sample data
data = {
    "col1": [1, 2, 3, 4, 7],
    "col2": [4, 5, 6, 9, 5],
    "col3": [7, 8, 12, 1, 11],
}

# create a DataFrame from the dictionary
df = pd.DataFrame(data)

# print the original DataFrame
print("Original DataFrame")
print(df)

# print the number of columns
print("\nNumber of columns:")
print(len(df.columns))
