# -------------------------------------------------
# File Name: 77_time_series_features.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Extracts year, month, day, quarter from datetime.
# -------------------------------------------------

import pandas as pd
import numpy as np

dates = pd.date_range("2024-01-01", periods=12, freq="ME")
df = pd.DataFrame({"date": dates, "sales": np.random.randint(80, 150, 12)})

print("=== ORIGINAL ===")
print(df)
print()

# Extract components
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["quarter"] = df["date"].dt.quarter
df["day_of_week"] = df["date"].dt.dayofweek
df["month_name"] = df["date"].dt.month_name()
df["is_month_start"] = df["date"].dt.is_month_start

print("=== EXTRACTED FEATURES ===")
print(df)
print()

# Period (monthly)
df["period"] = df["date"].dt.to_period("M")
print("=== to_period('M') ===")
print(df[["date", "period"]])
print()

# Week of year
df["week_of_year"] = df["date"].dt.isocalendar().week
print("=== week of year ===")
print(df[["date", "week_of_year"]])
