# -------------------------------------------------
# File Name: 14_index_operations.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: set_index, reset_index, rename index operations.
# -------------------------------------------------

# import libraries
import pandas as pd

# create a DataFrame with the country, city, and population data
df = pd.DataFrame({
    "country": ["USA", "USA", "UK", "UK"],
    "city": ["NYC", "LA", "London", "Manchester"],
    "pop": [8.4, 4.0, 9.0, 2.9],
})

# print the original DataFrame
print("=== ORIGINAL ===")
print(df)
print()

# set the 'country' column as index
df_idx = df.set_index("country")
print("=== set_index('country') ===")
print(df_idx)
print()

# reset the index to a column
df_reset = df_idx.reset_index()
print("=== reset_index() ===")
print(df_reset)
print()

# set the 'country' column as index and keep it as a column
df_idx2 = df.set_index("country", drop=False)
print("=== set_index(drop=False) ===")
print(df_idx2)
print()

# rename the index
# Set the 'country' column as index
df_idx = df.set_index("country")

# rename the index to 'nation'
df_idx.index = df_idx.index.rename("nation")
# print the DataFrame with the renamed index
print("=== index.rename('nation') ===")
print(df_idx)
print()

# set the 'country' and 'city' columns as index (MULTI-INDEX)
df_mi = df.set_index(["country", "city"])
print("=== MultiIndex (country, city) ===")
print(df_mi)
print()

# reset the index to a column
df_mi_reset = df_mi.reset_index()
print("=== reset_index() ===")
print(df_mi_reset)
print()

# set the 'country' and 'city' columns as index
df_mi = df.set_index(["country", "city"])
print("=== set_index(['country', 'city']) ===")
print(df_mi)
print()

# reset the index to a column
df_mi_reset = df_mi.reset_index()
print("=== reset_index() ===")
print(df_mi_reset)
print()

# set the 'country' and 'city' columns as index (MULTI-INDEX)
df_mi = df.set_index(["country", "city"])
print("=== set_index(['country', 'city']) ===")
print(df_mi)