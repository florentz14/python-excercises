# -------------------------------------------------
# File Name: 05_zscore_outliers.py
# Author: Florentino Báez
# Date: Statistics
# Description: Z-score, outlier detection, standardization.
# -------------------------------------------------

import numpy as np
from scipy import stats

data = np.array([10, 12, 14, 15, 16, 18, 20, 100])  # 100 is outlier

print("=== DATA ===")
print(data)
print()

# Z-score: z = (x - mean) / std
mean = np.mean(data)
std = np.std(data, ddof=1)
z_scores = (data - mean) / std

print("=== Z-SCORES ===")
for i, (val, z) in enumerate(zip(data, z_scores)):
    print(f"  {val}: z = {z:.2f}")
print()

# Outliers: |z| > 2 or |z| > 3
outliers_z2 = data[np.abs(z_scores) > 2]
outliers_z3 = data[np.abs(z_scores) > 3]
print("=== OUTLIERS (|z| > 2) ===")
print(outliers_z2)
print("Outliers (|z| > 3):", outliers_z3)
print()

# scipy.stats.zscore
z_scipy = stats.zscore(data)
print("=== stats.zscore ===")
print(z_scipy)
print()

# Standardization (mean=0, std=1)
standardized = (data - mean) / std
print("=== STANDARDIZED DATA ===")
print(standardized)
print(f"Mean: {np.mean(standardized):.4f}, Std: {np.std(standardized, ddof=1):.4f}")
print()

# IQR method (alternative to z-score)
q1, q3 = np.percentile(data, [25, 75])
iqr = q3 - q1
low = q1 - 1.5 * iqr
high = q3 + 1.5 * iqr
outliers_iqr = data[(data < low) | (data > high)]
print("=== IQR OUTLIER BOUNDS ===")
print(f"Bounds: [{low:.2f}, {high:.2f}]")
print("Outliers:", outliers_iqr)
