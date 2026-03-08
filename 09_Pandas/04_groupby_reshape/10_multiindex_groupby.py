# -------------------------------------------------
# File Name: 67_multiindex_groupby.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: GroupBy operations with MultiIndex.
# -------------------------------------------------

import pandas as pd
import numpy as np

# Sales by region and product
np.random.seed(42)
rows = []
for r in ["North", "South"]:
    for p in ["A", "B"]:
        for _ in range(3):
            rows.append({"region": r, "product": p, "sales": np.random.randint(50, 150)})
df = pd.DataFrame(rows)

# GroupBy with as_index=True → MultiIndex in result
gb = df.groupby(["region", "product"], as_index=True)["sales"]
agg = gb.agg(["sum", "mean", "count"])
print("=== groupby(['region','product']) — MultiIndex result ===")
print(agg)
print()

# unstack product to columns
wide = agg.unstack(level="product")
print("=== unstack('product') ===")
print(wide)
print()

# Aggregation with level (when index is MultiIndex)
df_mi = df.set_index(["region", "product"])
print("=== sum(level=0) — by region ===")
print(df_mi.groupby(level=0)["sales"].sum())
print()

# GroupBy with multiple agg
result = df.groupby(["region", "product"]).agg(total=("sales", "sum"), avg=("sales", "mean"))
print("=== Named aggregations ===")
print(result)
