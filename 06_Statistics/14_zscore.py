# -------------------------------------------------
# File Name: 14_zscore.py
# Author: Florentino Báez
# Description: Puntuación Z (z = (x - mean) / std).
# -------------------------------------------------

import numpy as np
from scipy import stats

data = np.array([10, 12, 14, 15, 16, 18, 20, 100])

print("=== DATA ===")
print(data)
print()

# Z-score: z = (x - mean) / std
mean = np.mean(data)
std = np.std(data, ddof=1)
z_scores = (data - mean) / std

print("=== Z-SCORES ===")
for val, z in zip(data, z_scores):
    print(f"  {val}: z = {z:.2f}")
print()

# scipy.stats.zscore
z_scipy = stats.zscore(data)
print("=== stats.zscore ===")
print(z_scipy)
