# -------------------------------------------------
# File Name: 79_time_series_forecasting_basics.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Rolling forecast, naive, pct_change forecasting.
# -------------------------------------------------

import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=20, freq="D")
trend = np.linspace(100, 150, 20)
noise = np.random.randn(20) * 5
sales = trend + noise
df = pd.DataFrame({"date": dates, "sales": sales}).set_index("date")

print("=== ORIGINAL ===")
print(df.head(10))
print()

# Naive forecast: last known value (shift)
df["naive_fcast"] = df["sales"].shift(1)
print("=== Naive (shift 1) ===")
print(df[["sales", "naive_fcast"]].head(6))
print()

# Rolling mean as baseline
df["rolling_fcast"] = df["sales"].rolling(3, min_periods=1).mean().shift(1)
print("=== Rolling mean forecast (lag 1) ===")
print(df[["sales", "rolling_fcast"]].head(8))
print()

# Simple growth rate
df["pct_change"] = df["sales"].pct_change()
print("=== pct_change() ===")
print(df[["sales", "pct_change"]].head(6))
print()

# Expanding mean (running baseline)
df["expanding_mean"] = df["sales"].expanding().mean()
print("=== Expanding mean ===")
print(df[["sales", "expanding_mean"]].head(6))
