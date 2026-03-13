# -------------------------------------------------
# File Name: 13_select_row_integer_index.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Selects a row using integer index position.
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

# print row at index position 2
print("\nIndex-2: Details")
print(df.iloc[[2]])
