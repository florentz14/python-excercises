# -------------------------------------------------
# File Name: 42_add_one_row.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Adds one row to a DataFrame.
# -------------------------------------------------

# Import pandas library
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]})

# Print the original DataFrame
print("Original DataFrame")
print(df)

# Add one row to the DataFrame
df.loc[len(df)] = [10, 11, 12]

# Print the DataFrame after adding one row
print("\nAfter add one row:")
print(df)
