# -------------------------------------------------
# File Name: 62_data_cleaning.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Strip spaces, fix capitalization, replace values, clip.
# -------------------------------------------------

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name": ["  Anna  ", "bob", "  CAROL  ", "david   "],
    "age": [25, 150, -5, 28],
    "status": ["active", "INACTIVE", "Active", "pending"],
})

print("=== ORIGINAL ===")
print(df)
print()

# Strip whitespace
df["name"] = df["name"].str.strip()
print("=== str.strip() ===")
print(df["name"])
print()

# Normalize capitalization
df["status"] = df["status"].str.lower().str.capitalize()
print("=== Normalize status ===")
print(df["status"])
print()

# Replace values (map)
status_map = {"Active": "A", "Inactive": "I", "Pending": "P"}
df["status_code"] = df["status"].map(status_map)
print("=== map to codes ===")
print(df[["status", "status_code"]])
print()

# Clip outliers (age between 0 and 120)
df["age_clipped"] = df["age"].clip(lower=0, upper=120)
print("=== clip(0, 120) ===")
print(df[["age", "age_clipped"]])
print()

# replace() for specific values
df["status_clean"] = df["status"].replace("Pending", "Paused")
print("=== replace ===")
print(df[["status", "status_clean"]])
