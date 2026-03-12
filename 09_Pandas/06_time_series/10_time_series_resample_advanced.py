# -------------------------------------------------
# File Name: 78_time_series_resample_advanced.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Advanced resampling and OHLC operations.
# -------------------------------------------------

import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=48, freq="2h")
df = pd.DataFrame({"ts": dates, "value": np.random.rand(48) * 100}).set_index("ts")

print("=== HOURLY-LIKE (2h freq) — first 6 ===")
print(df.head(6))
print()

# Resample to daily — mean
daily = df.resample("D").agg(["mean", "min", "max", "count"])
print("=== resample('D') — daily agg ===")
print(daily.head())
print()

# Resample to weekly
weekly = df.resample("W").mean()
print("=== resample('W') — weekly mean ===")
print(weekly)
print()

# Resample with ohlc (Open-High-Low-Close)
ohlc = df.resample("D")["value"].ohlc()
print("=== ohlc() ===")
print(ohlc.head())
print()

# Resample + fill method
filled = df.resample("6h").asfreq().ffill()
print("=== resample + ffill ===")
print(filled.head(8))
