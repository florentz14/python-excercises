# -------------------------------------------------
# File Name: 14_zscore.py
# Author: Florentino Báez
# Description: Standardizes observations with z-scores to express distance from the mean in standard deviations.
# -------------------------------------------------

import numpy as np # Fast numerical operations
from scipy import stats

data = np.array([10, 12, 14, 15, 16, 18, 20, 100]) # Data set

print("=== DATA ===")
print(data) # Data set
print()

# Z-score: z = (x - mean) / std
mean = np.mean(data) # Mean
std = np.std(data, ddof=1) # Standard deviation with Bessel's correction
z_scores = (data - mean) / std # Z-scores

print("=== Z-SCORES ===")
for val, z in zip(data, z_scores): # Z-scores
    print(f"  {val}: z = {z:.2f}")
print()

# scipy.stats.zscore
z_scipy = stats.zscore(data) # Z-scores
print("=== stats.zscore ===")
print(z_scipy) # Z-scores
