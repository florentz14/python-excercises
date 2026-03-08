# -------------------------------------------------
# File Name: 15_outlier_detection.py
# Author: Florentino Báez
# Description: Detects outliers using z-score thresholds and IQR bounds for method comparison.
# -------------------------------------------------

import numpy as np

data = np.array([10, 12, 14, 15, 16, 18, 20, 100])

print("=== DATA ===")
print(data)
print()

# Z-score method: |z| > 2 or |z| > 3
mean = np.mean(data)
std = np.std(data, ddof=1)
z_scores = (data - mean) / std
outliers_z2 = data[np.abs(z_scores) > 2]
outliers_z3 = data[np.abs(z_scores) > 3]

print("=== OUTLIERS (Z-SCORE) ===")
print("Outliers (|z| > 2):", outliers_z2)
print("Outliers (|z| > 3):", outliers_z3)
print()

# IQR method
q1, q3 = np.percentile(data, [25, 75])
iqr = q3 - q1
low = q1 - 1.5 * iqr
high = q3 + 1.5 * iqr
outliers_iqr = data[(data < low) | (data > high)]

print("=== IQR OUTLIER BOUNDS ===")
print(f"Bounds: [{low:.2f}, {high:.2f}]")
print("Outliers:", outliers_iqr)
