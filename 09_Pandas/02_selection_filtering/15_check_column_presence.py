# -------------------------------------------------
# File Name: 15_check_column_presence.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Checks whether specific columns are present in a DataFrame.
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

# check presence of selected columns
for col in ["col4", "col1"]:
    if col in df.columns:
        print(f"{col} is present in DataFrame.")
    else:
        print(f"{col} is not present in DataFrame.")
