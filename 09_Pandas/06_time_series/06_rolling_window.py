# -------------------------------------------------
# File Name: 68_rolling_window.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Rolling mean and rolling std window functions.
# -------------------------------------------------

import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=20, freq="D")
sales = np.random.randint(80, 150, 20)
df = pd.DataFrame({"date": dates, "sales": sales}).set_index("date")

print("=== ORIGINAL ===")
print(df.head(10))
print()

# Rolling mean (window=3)
df["rolling_3"] = df["sales"].rolling(window=3).mean()
print("=== rolling(3).mean() ===")
print(df[["sales", "rolling_3"]].head(10))
print()

# Rolling std
df["rolling_std"] = df["sales"].rolling(3).std()
print("=== rolling(3).std() ===")
print(df[["sales", "rolling_std"]].head(8))
print()

# min_periods — reduce NaN at start
df["rolling_3_min1"] = df["sales"].rolling(3, min_periods=1).mean()
print("=== rolling(3, min_periods=1) ===")
print(df[["sales", "rolling_3_min1"]].head(5))
print()

# Rolling sum
df["rolling_sum"] = df["sales"].rolling(4).sum()
print("=== rolling(4).sum() ===")
print(df[["sales", "rolling_sum"]].head(6))
