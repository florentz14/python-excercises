# -------------------------------------------------
# File Name: 35_time_series_apple_stock.py
# Author: Florentino Báez
# Date: Pandas
# Description: Time Series Analysis of Apple Stock Data. Practice DatetimeIndex,
#              resample(), rolling windows, pct_change(), and date-based filtering
#              on stock price data.
# -------------------------------------------------

import pandas as pd
import numpy as np

# -------------------------------------------------
# Create DataFrame with DatetimeIndex (business days for 6 months)
# -------------------------------------------------
np.random.seed(42)
dates = pd.bdate_range(start="2024-01-01", end="2024-06-30", freq="B")
n = len(dates)

# Generate realistic stock prices using cumulative random walk starting from ~150
returns = np.random.normal(0.0005, 0.015, n)
close = 150 * np.exp(np.cumsum(returns))
# Derive Open, High, Low from Close for realism
open_price = np.roll(close, 1)
open_price[0] = 150
high = np.maximum(open_price, close) * (1 + np.abs(np.random.normal(0, 0.005, n)))
low = np.minimum(open_price, close) * (1 - np.abs(np.random.normal(0, 0.005, n)))
volume = np.random.randint(50_000_000, 120_000_000, n)

df = pd.DataFrame({
    "Open": open_price,
    "High": high,
    "Low": low,
    "Close": close,
    "Volume": volume
}, index=dates)
df.index.name = "Date"
print("Apple stock data (first 5 rows):")
print(df.head())
print()

# -------------------------------------------------
# Select data for a specific month using string indexing (use .loc for index)
# -------------------------------------------------
jan_2024 = df.loc["2024-01"]
print("Data for January 2024:")
print(jan_2024.head())
print()

# -------------------------------------------------
# Resample to weekly data (mean)
# -------------------------------------------------
weekly = df.resample("W").mean()
print("Weekly resampled (mean):")
print(weekly.head())
print()

# -------------------------------------------------
# Resample to monthly data (OHLC-like: first open, max high, min low, last close)
# -------------------------------------------------
monthly_ohlc = df.resample("ME").agg({
    "Open": "first",
    "High": "max",
    "Low": "min",
    "Close": "last",
    "Volume": "sum"
})
print("Monthly OHLC-style resample:")
print(monthly_ohlc)
print()

# -------------------------------------------------
# Calculate daily returns using pct_change()
# -------------------------------------------------
df["Daily_Return"] = df["Close"].pct_change()
print("Daily returns (first 5):")
print(df[["Close", "Daily_Return"]].head())
print()

# -------------------------------------------------
# Calculate 20-day rolling mean and rolling std
# -------------------------------------------------
df["Rolling_Mean_20"] = df["Close"].rolling(window=20).mean()
df["Rolling_Std_20"] = df["Close"].rolling(window=20).std()
print("20-day rolling mean and std (sample):")
print(df[["Close", "Rolling_Mean_20", "Rolling_Std_20"]].tail(5))
print()

# -------------------------------------------------
# Find the day with highest volume
# -------------------------------------------------
day_max_vol = df["Volume"].idxmax()
print("Day with highest volume:", day_max_vol, "Volume:", df.loc[day_max_vol, "Volume"])
print()

# -------------------------------------------------
# Find the day with highest daily return
# -------------------------------------------------
day_max_return = df["Daily_Return"].idxmax()
print("Day with highest daily return:", day_max_return, "Return:", df.loc[day_max_return, "Daily_Return"])
print()

# -------------------------------------------------
# Calculate cumulative return
# -------------------------------------------------
df["Cumulative_Return"] = (1 + df["Daily_Return"]).cumprod() - 1
print("Cumulative return at end of period:", df["Cumulative_Return"].iloc[-1])
print()

# -------------------------------------------------
# Show statistics with describe()
# -------------------------------------------------
print("Describe (numeric columns):")
print(df.describe())
