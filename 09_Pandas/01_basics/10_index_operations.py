# -------------------------------------------------
# File Name: 65_index_operations.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: set_index, reset_index, rename index operations.
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "country": ["USA", "USA", "UK", "UK"],
    "city": ["NYC", "LA", "London", "Manchester"],
    "pop": [8.4, 4.0, 9.0, 2.9],
})

print("=== ORIGINAL ===")
print(df)
print()

# set_index
df_idx = df.set_index("country")
print("=== set_index('country') ===")
print(df_idx)
print()

# reset_index — index back to column
df_reset = df_idx.reset_index()
print("=== reset_index() ===")
print(df_reset)
print()

# set_index with drop=False
df_idx2 = df.set_index("country", drop=False)
print("=== set_index(drop=False) ===")
print(df_idx2)
print()

# rename index
df_idx = df.set_index("country")
df_idx.index = df_idx.index.rename("nation")
print("=== index.rename('nation') ===")
print(df_idx)
print()

# Multi-index from columns
df_mi = df.set_index(["country", "city"])
print("=== MultiIndex (country, city) ===")
print(df_mi)
