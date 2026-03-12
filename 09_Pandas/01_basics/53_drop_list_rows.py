# -------------------------------------------------
# File Name: 53_drop_list_rows.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Drops a list of rows from a DataFrame.
# -------------------------------------------------

# Import pandas library
import pandas as pd

# Create a dictionary with the data
data = {"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]}

# Create a DataFrame with the data
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame")
print(df)

# Drop the 2nd and 4th rows
df = df.drop([2, 4])

# Print the new DataFrame
print("\nNew DataFrame after removing 2nd & 4th rows:")
print(df)
