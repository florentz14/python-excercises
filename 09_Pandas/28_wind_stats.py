# -------------------------------------------------
# File Name: 28_wind_stats.py
# Author: Florentino Báez
# Date: Pandas
# Description: Statistical Analysis of Wind Data. Compute daily, monthly, and
#              location-based wind statistics including mean, std, min, max,
#              correlation, and rolling averages.
# -------------------------------------------------

import pandas as pd
import numpy as np

# Create 30 days of datetime index
dates = pd.date_range(start="2024-01-01", periods=30, freq="D")

# Create sample wind speed data for 4 weather stations (values in mph or m/s)
np.random.seed(42)
data = {
    "station_1": np.random.uniform(5, 25, 30).round(1),
    "station_2": np.random.uniform(4, 22, 30).round(1),
    "station_3": np.random.uniform(6, 24, 30).round(1),
    "station_4": np.random.uniform(5, 23, 30).round(1),
}

df = pd.DataFrame(data, index=dates)
df.index.name = "Date"

print("=" * 60)
print("WIND STATS - STATISTICAL ANALYSIS")
print("=" * 60)

# Use describe() for overall statistics
print("\n--- Overall statistics (describe) ---")
print(df.describe())

# Calculate daily mean across all stations
df["daily_mean"] = df[["station_1", "station_2", "station_3", "station_4"]].mean(axis=1)
print("\n--- Daily mean wind speed across all stations ---")
print(df["daily_mean"].head(10))

# Find the windiest day (highest mean across stations)
windiest_day = df["daily_mean"].idxmax()
print(f"\n--- Windiest day: {windiest_day.date()} (mean: {df['daily_mean'].max():.2f}) ---")

# Calculate monthly statistics using resample() (30 days = ~1 month)
print("\n--- Monthly statistics (resample) ---")
monthly = df.resample("ME")[["station_1", "station_2", "station_3", "station_4"]].agg(["mean", "std", "min", "max"])
print(monthly)

# Compute correlation between stations using corr()
print("\n--- Correlation between stations ---")
print(df[["station_1", "station_2", "station_3", "station_4"]].corr())

# Calculate rolling 7-day average
df["rolling_7d"] = df["daily_mean"].rolling(window=7, min_periods=1).mean()
print("\n--- Rolling 7-day average (last 10 days) ---")
print(df["rolling_7d"].tail(10))

# Find min and max wind speed per station
print("\n--- Min and max wind speed per station ---")
print(df[["station_1", "station_2", "station_3", "station_4"]].agg(["min", "max"]))

# Use quantile() to find percentiles
print("\n--- Percentiles (25%, 50%, 75%) per station ---")
print(df[["station_1", "station_2", "station_3", "station_4"]].quantile([0.25, 0.5, 0.75]))

# Standard deviation per station
print("\n--- Standard deviation per station ---")
print(df[["station_1", "station_2", "station_3", "station_4"]].std())

print("\nDone.")
