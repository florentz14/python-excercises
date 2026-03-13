# -------------------------------------------------
# File Name: 12_delete_rows_by_value.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Deletes rows based on a column value condition.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a DataFrame with sample data
df = pd.DataFrame(
    {
        "col1": [1, 4, 3, 4, 5],
        "col2": [4, 5, 6, 7, 8],
        "col3": [7, 8, 9, 0, 1],
    }
)

# print the original DataFrame
print("Original DataFrame")
print(df)

# delete rows where col2 equals 5
df = df[df["col2"] != 5]

# print the new DataFrame
print("\nNew DataFrame")
print(df)
