# -------------------------------------------------
# File Name: 10_drop.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Drops rows, columns, and duplicates.
# -------------------------------------------------

import pandas as pd

# Create a DataFrame with duplicates
df = pd.DataFrame({
    "a": [1, 2, 2, 3],
    "b": [4, 5, 5, 6],
    "c": [7, 8, 9, 10],
})

# Drop column 'b'
df_no_b = df.drop(columns=["b"])
print("Without column 'b':\n", df_no_b)

# Drop rows 0 and 1
df_no_rows = df.drop(index=[0, 1])
print("\nWithout rows 0 and 1:\n", df_no_rows)

# Drop duplicates (remove duplicate rows)
# Create a DataFrame with duplicates
df_dup = pd.DataFrame({"x": [1, 1, 2, 2], "y": [3, 3, 4, 5]})

# Drop duplicates (remove duplicate rows)
df_unique = df_dup.drop_duplicates()
# Print the DataFrame without duplicates
print("\nWithout duplicates:\n", df_unique)
