# -------------------------------------------------
# File Name: 88_sales_forecast_project.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Sales forecasting with rolling methods.
# -------------------------------------------------

from pathlib import Path

import pandas as pd
import numpy as np

DATA = Path(__file__).parent.parent / "data"
df = pd.read_csv(DATA / "store_sales.csv", parse_dates=["date"])
df["revenue"] = df["quantity"] * df["unit_price"]

# Daily revenue
daily = df.groupby("date")["revenue"].sum().reset_index()
daily = daily.sort_values("date")

print("=== DAILY REVENUE ===")
print(daily.head(10))
print()

# Rolling 3-day average
daily["rolling_3"] = daily["revenue"].rolling(3, min_periods=1).mean()
daily["rolling_7"] = daily["revenue"].rolling(7, min_periods=1).mean()

print("=== ROLLING AVERAGES ===")
print(daily[["date", "revenue", "rolling_3", "rolling_7"]].tail(10))
print()

# Naive forecast (next day = last day)
daily["naive_fcast"] = daily["revenue"].shift(1)

# Moving average forecast (next = mean of last 3)
daily["ma3_fcast"] = daily["revenue"].rolling(3).mean().shift(1)
print("=== FORECAST COLUMNS ===")
print(daily[["date", "revenue", "naive_fcast", "ma3_fcast"]].tail(5))
print()

# Summary stats
print(f"Total revenue: ${daily['revenue'].sum():.2f}")
print(f"Avg daily: ${daily['revenue'].mean():.2f}")
