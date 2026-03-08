# -------------------------------------------------
# File Name: 69_expanding_window.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Expanding statistics window functions.
# -------------------------------------------------

import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=10, freq="D")
values = np.cumsum(np.random.randint(1, 10, 10))
df = pd.DataFrame({"date": dates, "cumulative": values})

print("=== CUMULATIVE DATA ===")
print(df)
print()

# Expanding mean — running average from start
df["exp_mean"] = df["cumulative"].expanding().mean()
df["exp_sum"] = df["cumulative"].expanding().sum()
print("=== expanding().mean() & sum() ===")
print(df)
print()

# Expanding min/max
df["exp_max"] = df["cumulative"].expanding().max()
print("=== expanding().max() ===")
print(df[["cumulative", "exp_max"]])
print()

# Use case: running total and running avg
df["running_total"] = df["cumulative"].expanding().sum()
df["running_avg"] = df["cumulative"].expanding().mean()
print("=== Running total & avg ===")
print(df[["cumulative", "running_total", "running_avg"]])
