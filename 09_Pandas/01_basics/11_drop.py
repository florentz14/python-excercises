# -------------------------------------------------
# File Name: 11_drop.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Drops rows, columns, and duplicates.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a DataFrame with duplicates
df = pd.DataFrame({
    "a": [1, 2, 2, 3],
    "b": [4, 5, 5, 6],
    "c": [7, 8, 9, 10],
})

# drop column 'b'
df_no_b = df.drop(columns=["b"])
print("Without column 'b':\n", df_no_b)

# drop rows 0 and 1
df_no_rows = df.drop(index=[0, 1])
print("\nWithout rows 0 and 1:\n", df_no_rows)

# drop duplicates (remove duplicate rows)
# create a DataFrame with duplicates
df_dup = pd.DataFrame({"x": [1, 1, 2, 2], "y": [3, 3, 4, 5]})

# drop duplicates (remove duplicate rows)
df_unique = df_dup.drop_duplicates()
# print the DataFrame without duplicates
print("\nWithout duplicates:\n", df_unique)
