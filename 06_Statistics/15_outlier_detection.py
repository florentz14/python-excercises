# -------------------------------------------------
# File Name: 15_outlier_detection.py
# Author: Florentino Báez
# Description: Detects outliers using z-score thresholds and IQR bounds for method comparison.
# -------------------------------------------------

import numpy as np # Fast numerical operations

data = np.array([10, 12, 14, 15, 16, 18, 20, 100]) # Data set

print("=== DATA ===")
print(data) # Data set
print()

# Z-score method: |z| > 2 or |z| > 3
mean = np.mean(data) # Mean
std = np.std(data, ddof=1) # Standard deviation with Bessel's correction
z_scores = (data - mean) / std
outliers_z2 = data[np.abs(z_scores) > 2] # Outliers
outliers_z3 = data[np.abs(z_scores) > 3] # Outliers

print("=== OUTLIERS (Z-SCORE) ===")
print("Outliers (|z| > 2):", outliers_z2) # Outliers
print("Outliers (|z| > 3):", outliers_z3) # Outliers
print()

# IQR method
q1, q3 = np.percentile(data, [25, 75]) # Q1 and Q3
iqr = q3 - q1 # IQR
low = q1 - 1.5 * iqr # Lower bound (1.5 * IQR rule)
high = q3 + 1.5 * iqr # Upper bound (1.5 * IQR rule)
outliers_iqr = data[(data < low) | (data > high)] # Outliers    

print("=== IQR OUTLIER BOUNDS ===")
print(f"Bounds: [{low:.2f}, {high:.2f}]") # Bounds
print("Outliers:", outliers_iqr) # Outliers IQR
