# -------------------------------------------------
# File Name: 16_get_row_value.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Retrieves values for specific rows by integer position.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a dictionary with sample data
data = {"col1": [1, 2, 3, 4, 7], "col2": [4, 5, 6, 9, 5], "col3": [7, 8, 12, 1, 11]}

# create a DataFrame from the dictionary
df = pd.DataFrame(data)

# print the original DataFrame
print("Original DataFrame")
print(df)

# print row values by position
print("\nValue of Row 0")
print(df.iloc[0])
print("\nValue of Row 4")
print(df.iloc[3])
