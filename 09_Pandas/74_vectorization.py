# -------------------------------------------------
# File Name: 74_vectorization.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Vectorized operations vs loops for performance.
# -------------------------------------------------

import pandas as pd
import numpy as np
import time

np.random.seed(42)
n = 100_000
df = pd.DataFrame({"a": np.random.rand(n), "b": np.random.rand(n)})

# Loop (slow)
start = time.perf_counter()
result_loop = []
for i in range(len(df)):
    result_loop.append(df["a"].iloc[i] + df["b"].iloc[i])
elapsed_loop = time.perf_counter() - start

# Vectorized (fast)
start = time.perf_counter()
result_vec = df["a"] + df["b"]
elapsed_vec = time.perf_counter() - start

print("=== VECTORIZATION (n=100k) ===")
print(f"Loop:    {elapsed_loop:.4f} s")
print(f"Vector:  {elapsed_vec:.4f} s")
print(f"Speedup: {elapsed_loop / elapsed_vec:.0f}x")
print()

# More vectorized patterns
df["c"] = df["a"] * 2 + df["b"] ** 2
df["d"] = np.where(df["a"] > 0.5, "high", "low")
df["e"] = df["a"].apply(lambda x: x * 2)  # apply is slower
print("=== Sample (vector ops) ===")
print(df.head())
print()

# pd.cut for tier (vectorized)
df["tier"] = pd.cut(df["a"], bins=[0, 0.33, 0.66, 1.01], labels=["low", "mid", "high"])
print("=== pd.cut for tiers ===")
print(df[["a", "tier"]].head(10))
