# -------------------------------------------------
# File Name: 75_memory_optimization.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: category dtype and memory_usage optimization.
# -------------------------------------------------

import pandas as pd
import numpy as np

# Object column with few unique values
df = pd.DataFrame({
    "id": range(1000),
    "status": ["active", "inactive", "pending"] * 333 + ["active"],
    "region": ["North", "South"] * 500,
})

print("=== MEMORY (before) ===")
print(df.memory_usage(deep=True))
print(f"Total: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")
print()

# Convert to category
df["status_cat"] = df["status"].astype("category")
df["region_cat"] = df["region"].astype("category")
print("=== MEMORY (after category) ===")
print(df[["status_cat", "region_cat"]].memory_usage(deep=True))
print()

# Compare
obj_mem = df["status"].memory_usage(deep=True)
cat_mem = df["status_cat"].memory_usage(deep=True)
print(f"status: object={obj_mem} B, category={cat_mem} B")
print()

# Downcast integers
df_int = pd.DataFrame({"a": np.arange(1000, dtype=np.int64)})
print("=== Downcast int64 -> int16 ===")
df_int["a_16"] = pd.to_numeric(df_int["a"], downcast="integer")
print(df_int.dtypes)
print()

# memory_usage by dtype
print("=== memory_usage(deep=True) by column ===")
print(df.memory_usage(deep=True))
