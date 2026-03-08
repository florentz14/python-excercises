# -------------------------------------------------
# File Name: 85_encoding_features.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: One-hot, get_dummies, label encoding.
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "color": ["red", "blue", "green", "red", "blue"],
    "size": ["S", "M", "L", "M", "S"],
})

print("=== ORIGINAL ===")
print(df)
print()

# One-hot (get_dummies)
dummies = pd.get_dummies(df[["color", "size"]])
print("=== pd.get_dummies() ===")
print(dummies)
print()

# One-hot with prefix
dummies_pref = pd.get_dummies(df, columns=["color"], prefix="col")
print("=== prefix ===")
print(dummies_pref)
print()

# Label encoding (manual map)
color_map = {"red": 0, "blue": 1, "green": 2}
df["color_code"] = df["color"].map(color_map)
print("=== map (label encoding) ===")
print(df[["color", "color_code"]])
print()

# pd.Categorical.codes
df["size_code"] = df["size"].astype("category").cat.codes
print("=== category.codes ===")
print(df[["size", "size_code"]])
