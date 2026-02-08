# -------------------------------------------------
# File Name: 36_time_series_financial_data.py
# Author: Florentino Báez
# Date: Pandas
# Description: Generate and Analyze Financial Time Series Data. Practice creating
#              datetime ranges, shifting data, calculating moving averages, and
#              computing financial metrics.
# -------------------------------------------------

import pandas as pd
import numpy as np

# -------------------------------------------------
# Create DatetimeIndex with pd.date_range (1 year of daily data)
# -------------------------------------------------
np.random.seed(123)
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="B")
n = len(dates)

# Create DataFrame with SP500, NASDAQ, DOW using cumsum of random returns
sp_returns = np.random.normal(0.0003, 0.01, n)
nasdaq_returns = np.random.normal(0.0004, 0.012, n)
dow_returns = np.random.normal(0.00025, 0.009, n)

df = pd.DataFrame({
    "SP500": 4000 * np.exp(np.cumsum(sp_returns)),
    "NASDAQ": 12000 * np.exp(np.cumsum(nasdaq_returns)),
    "DOW": 33000 * np.exp(np.cumsum(dow_returns))
}, index=dates)
df.index.name = "Date"
print("Financial data (first 5 rows):")
print(df.head())
print()

# -------------------------------------------------
# Use shift() to create lagged columns
# -------------------------------------------------
df["SP500_Lag1"] = df["SP500"].shift(1)
df["SP500_Lag5"] = df["SP500"].shift(5)
print("Lagged columns (sample):")
print(df[["SP500", "SP500_Lag1", "SP500_Lag5"]].head(7))
print()

# -------------------------------------------------
# Calculate daily returns for all indices
# -------------------------------------------------
df["SP500_Return"] = df["SP500"].pct_change()
df["NASDAQ_Return"] = df["NASDAQ"].pct_change()
df["DOW_Return"] = df["DOW"].pct_change()
print("Daily returns (sample):")
print(df[["SP500_Return", "NASDAQ_Return", "DOW_Return"]].head(5))
print()

# -------------------------------------------------
# Calculate correlation between indices using corr()
# -------------------------------------------------
returns_df = df[["SP500_Return", "NASDAQ_Return", "DOW_Return"]].dropna()
corr_matrix = returns_df.corr()
print("Correlation between index returns:")
print(corr_matrix)
print()

# -------------------------------------------------
# Calculate 30-day and 90-day moving averages
# -------------------------------------------------
df["SP500_MA30"] = df["SP500"].rolling(window=30).mean()
df["SP500_MA90"] = df["SP500"].rolling(window=90).mean()
print("30-day and 90-day moving averages for SP500 (last 5):")
print(df[["SP500", "SP500_MA30", "SP500_MA90"]].tail(5))
print()

# -------------------------------------------------
# Use expanding() for cumulative statistics
# -------------------------------------------------
df["SP500_Expanding_Mean"] = df["SP500"].expanding().mean()
df["SP500_Expanding_Max"] = df["SP500"].expanding().max()
print("Expanding mean and max (last 5):")
print(df[["SP500", "SP500_Expanding_Mean", "SP500_Expanding_Max"]].tail(5))
print()

# -------------------------------------------------
# Calculate drawdown (current value / running max - 1)
# -------------------------------------------------
df["SP500_RunningMax"] = df["SP500"].expanding().max()
df["SP500_Drawdown"] = df["SP500"] / df["SP500_RunningMax"] - 1
print("SP500 drawdown (sample, last 5):")
print(df[["SP500", "SP500_RunningMax", "SP500_Drawdown"]].tail(5))
print()

# -------------------------------------------------
# Resample to monthly frequency, compute monthly returns
# -------------------------------------------------
monthly = df[["SP500", "NASDAQ", "DOW"]].resample("ME").last()
monthly_returns = monthly.pct_change()
print("Monthly returns (sample):")
print(monthly_returns.head(5))
print()

# -------------------------------------------------
# Find the best and worst month for each index
# -------------------------------------------------
sp_monthly_ret = df["SP500"].resample("ME").last().pct_change()
best_month_sp = sp_monthly_ret.idxmax()
worst_month_sp = sp_monthly_ret.idxmin()
print("SP500 best month:", best_month_sp, "Return:", sp_monthly_ret[best_month_sp])
print("SP500 worst month:", worst_month_sp, "Return:", sp_monthly_ret[worst_month_sp])
print()

# -------------------------------------------------
# Rolling correlation between two indices
# -------------------------------------------------
df["Rolling_Corr_SP_NASDAQ"] = (
    df["SP500_Return"].rolling(window=30).corr(df["NASDAQ_Return"])
)
print("30-day rolling correlation SP500 vs NASDAQ (last 5):")
print(df[["SP500_Return", "NASDAQ_Return", "Rolling_Corr_SP_NASDAQ"]].tail(5))
print()

# Summary statistics
print("Describe (key columns):")
print(df[["SP500", "NASDAQ", "DOW", "SP500_Return", "SP500_Drawdown"]].describe())
