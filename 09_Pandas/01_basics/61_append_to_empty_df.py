# -------------------------------------------------
# File Name: 61_append_to_empty_dataframe.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Appends data to an empty DataFrame.
# -------------------------------------------------

# import libraries
import pandas as pd

# create an empty DataFrame
df = pd.DataFrame()

# print the original DataFrame
print("Original DataFrame:")
print(df)

# append some data to the DataFrame
df = pd.concat([df, pd.DataFrame({"col1": [0, 1, 2], "col2": [0, 1, 2]})], ignore_index=True)
print("\nAfter appending some data:")
print(df)
