# -------------------------------------------------
# File Name: 64_outlier_detection.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: IQR and z-score based outlier detection.
# -------------------------------------------------

import pandas as pd
import numpy as np

np.random.seed(42)
values = np.random.normal(100, 15, 100)
values[0], values[1], values[2] = 200, 250, 30  # outliers
df = pd.DataFrame({"value": values})

print("=== SAMPLE ===")
print(df["value"].describe())
print()

# IQR method
q1 = df["value"].quantile(0.25)
q3 = df["value"].quantile(0.75)
iqr = q3 - q1
low = q1 - 1.5 * iqr
high = q3 + 1.5 * iqr

print("=== IQR METHOD ===")
print(f"Q1={q1:.2f} Q3={q3:.2f} IQR={iqr:.2f}")
print(f"Bounds: [{low:.2f}, {high:.2f}]")
outliers_iqr = df[(df["value"] < low) | (df["value"] > high)]
print(f"Outliers ({len(outliers_iqr)}): {outliers_iqr['value'].tolist()}")
print()

# Z-score method
mean = df["value"].mean()
std = df["value"].std()
df["zscore"] = (df["value"] - mean) / std
outliers_z = df[np.abs(df["zscore"]) > 2]
print("=== Z-SCORE (|z| > 2) ===")
print(outliers_z[["value", "zscore"]])
print()

# clip outliers
df["clipped"] = df["value"].clip(lower=low, upper=high)
print("=== CLIP OUTLIERS ===")
print(df[["value", "clipped"]].head(5))
