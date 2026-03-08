# -------------------------------------------------
# File Name: 86_scaling_features.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Min-max, z-score, robust scaling.
# -------------------------------------------------

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "a": [1, 2, 3, 4, 5],
    "b": [100, 200, 300, 400, 500],
})

print("=== ORIGINAL ===")
print(df)
print()

# Min-Max (0 to 1)
df["a_minmax"] = (df["a"] - df["a"].min()) / (df["a"].max() - df["a"].min())
print("=== Min-Max scaling ===")
print(df[["a", "a_minmax"]])
print()

# Z-score (standardization)
df["a_zscore"] = (df["a"] - df["a"].mean()) / df["a"].std()
print("=== Z-score ===")
print(df[["a", "a_zscore"]])
print()

# Robust scale (using IQR)
q1, q3 = df["a"].quantile(0.25), df["a"].quantile(0.75)
iqr = q3 - q1
df["a_robust"] = (df["a"] - df["a"].median()) / iqr
print("=== Robust (median, IQR) ===")
print(df[["a", "a_robust"]])
print()

# Log transform
df["b_log"] = np.log1p(df["b"])
print("=== log1p(b) ===")
print(df[["b", "b_log"]])
