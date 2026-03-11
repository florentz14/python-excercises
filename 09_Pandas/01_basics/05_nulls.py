# -------------------------------------------------
# File Name: 07_nulls.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Handles null values with isna, fillna, and dropna.
# -------------------------------------------------

import pandas as pd
import numpy as np

# Create a DataFrame with nulls
df = pd.DataFrame({
    "a": [1, np.nan, 3, 4],
    "b": [5, 6, np.nan, 8],
    "c": [9, 10, 11, 12],
})

print("DataFrame with nulls:\n", df)

# Print the nulls in the DataFrame
print("\nDetect nulls (isna):\n", df.isna())

# Print the count of nulls per column
print("\nCount nulls per column:\n", df.isna().sum())

# Drop the rows with nulls
df_no_nulls = df.dropna()
print("\nNo null rows (dropna):\n", df_no_nulls)

# Fill the nulls with 0
df_filled = df.fillna(0)
print("\nFill with 0 (fillna):\n", df_filled)
