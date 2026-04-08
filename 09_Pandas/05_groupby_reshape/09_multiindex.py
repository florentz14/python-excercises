# -------------------------------------------------
# File Name: 66_multiindex.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: MultiIndex basics: hierarchical indexing, stack/unstack.
# -------------------------------------------------

import pandas as pd
import numpy as np

# Create MultiIndex from tuples
index = pd.MultiIndex.from_tuples(
    [("USA", "NYC"), ("USA", "LA"), ("UK", "London"), ("UK", "Manchester")],
    names=["country", "city"],
)
df = pd.DataFrame({"pop": [8.4, 4.0, 9.0, 2.9], "area": [780, 500, 1570, 115]}, index=index)

print("=== MultiIndex DataFrame ===")
print(df)
print()

# Selection by first level
print("=== .loc['USA'] ===")
print(df.loc["USA"])
print()

# Selection by both levels
print("=== .loc[('USA','NYC')] ===")
print(df.loc[("USA", "NYC")])
print()

# xs — cross-section
print("=== xs('UK', level='country') ===")
print(df.xs("UK", level="country"))
print()

# stack / unstack
df_flat = df.reset_index()
pivot = df_flat.pivot_table(index="country", columns="city", values="pop")
print("=== Pivot (wide) ===")
print(pivot)
stacked = pivot.stack()
print("=== stack() -> Series with MultiIndex ===")
print(stacked)
print()

# swaplevel
df_swapped = df.swaplevel(0, 1)
print("=== swaplevel ===")
print(df_swapped)
