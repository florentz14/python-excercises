# -------------------------------------------------
# File Name: 65_index_operations.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: set_index, reset_index, rename index operations.
# -------------------------------------------------

import pandas as pd

# Create a DataFrame with the country, city, and population data
df = pd.DataFrame({
    "country": ["USA", "USA", "UK", "UK"],
    "city": ["NYC", "LA", "London", "Manchester"],
    "pop": [8.4, 4.0, 9.0, 2.9],
})

# Print the original DataFrame
print("=== ORIGINAL ===")
print(df)
print()

# set_index (set the 'country' column as index)
df_idx = df.set_index("country")
print("=== set_index('country') ===")
print(df_idx)
print()

# reset_index — index back to column (reset the index to a column)
df_reset = df_idx.reset_index()
print("=== reset_index() ===")
print(df_reset)
print()

# set_index with drop=False (set the 'country' column as index and keep it as a column)
df_idx2 = df.set_index("country", drop=False)
print("=== set_index(drop=False) ===")
print(df_idx2)
print()

# rename index (rename the index)
# Set the 'country' column as index
df_idx = df.set_index("country")

# Rename the index to 'nation'
df_idx.index = df_idx.index.rename("nation")
# Print the DataFrame with the renamed index
print("=== index.rename('nation') ===")
print(df_idx)
print()

# Multi-index from columns (set the 'country' and 'city' columns as index) (MULTI-INDEX)
df_mi = df.set_index(["country", "city"])
print("=== MultiIndex (country, city) ===")
print(df_mi)
print()

# Reset the index to a column (reset the index to a column)
df_mi_reset = df_mi.reset_index()
print("=== reset_index() ===")
print(df_mi_reset)
print()

# Set the 'country' and 'city' columns as index
df_mi = df.set_index(["country", "city"])
print("=== set_index(['country', 'city']) ===")
print(df_mi)
print()

# Reset the index to a column (reset the index to a column)
df_mi_reset = df_mi.reset_index()
print("=== reset_index() ===")
print(df_mi_reset)
print()

# Set the 'country' and 'city' columns as index (MULTI-INDEX)
df_mi = df.set_index(["country", "city"])
print("=== set_index(['country', 'city']) ===")
print(df_mi)