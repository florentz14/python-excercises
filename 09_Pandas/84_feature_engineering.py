# -------------------------------------------------
# File Name: 84_feature_engineering.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Derived features, lag, diff for feature engineering.
# -------------------------------------------------

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "price": [10, 20, 30, 40, 50],
    "quantity": [2, 4, 1, 3, 5],
    "date": pd.to_datetime(["2024-01-01", "2024-01-15", "2024-02-01", "2024-02-15", "2024-03-01"]),
})

print("=== ORIGINAL ===")
print(df)
print()

# Derived: total
df["total"] = df["price"] * df["quantity"]
print("=== total = price * quantity ===")
print(df[["price", "quantity", "total"]])
print()

# Ratio
df["price_per_unit_avg"] = df["total"] / df["quantity"]
print("=== price_per_unit_avg ===")
print(df["price_per_unit_avg"])
print()

# Lag
df["price_lag1"] = df["price"].shift(1)
df["price_diff"] = df["price"].diff()
print("=== lag & diff ===")
print(df[["price", "price_lag1", "price_diff"]])
print()

# Date features
df["day_of_year"] = df["date"].dt.dayofyear
df["month"] = df["date"].dt.month
print("=== date features ===")
print(df[["date", "day_of_year", "month"]])
