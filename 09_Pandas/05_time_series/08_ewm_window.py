# -------------------------------------------------
# File Name: 70_ewm_window.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Exponential weighted moving average.
# -------------------------------------------------

import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=15, freq="D")
prices = 100 + np.cumsum(np.random.randn(15) * 2)
df = pd.DataFrame({"date": dates, "price": prices}).set_index("date")

print("=== PRICE SERIES ===")
print(df.head(10))
print()

# ewm — span=5 (halflife-like)
df["ewm_5"] = df["price"].ewm(span=5, adjust=False).mean()
print("=== ewm(span=5).mean() ===")
print(df[["price", "ewm_5"]].head(10))
print()

# span vs alpha
# span ≈ 2/alpha - 1  →  span=5  →  alpha ≈ 0.33
df["ewm_alpha"] = df["price"].ewm(alpha=0.3, adjust=False).mean()
print("=== ewm(alpha=0.3) ===")
print(df[["price", "ewm_alpha"]].head(8))
print()

# adjust=True (default) — recursive form
df["ewm_adjust"] = df["price"].ewm(span=5, adjust=True).mean()
print("=== ewm(adjust=True) ===")
print(df[["price", "ewm_adjust"]].head(6))
