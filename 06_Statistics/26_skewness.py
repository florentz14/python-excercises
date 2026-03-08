# -------------------------------------------------
# File Name: 26_skewness.py
# Description: Computes skewness to assess distribution asymmetry (left- or right-tailed).
# -------------------------------------------------

import numpy as np  # Numerical arrays and vectorized operations
from scipy import stats  # Statistical tests and probability distributions

data = np.array([12, 15, 18, 22, 25, 25, 28, 30, 33, 40]) # Data set

print("=== DATA ===")
print(data) # print the data set
print()

# Skewness
skew = stats.skew(data) # Skewness
print("=== SKEWNESS ===")
print(f"Skewness: {skew:.4f}") # print the skewness
print("  skew > 0: right-tailed (positive skew)") # print the skewness
print("  skew < 0: left-tailed (negative skew)") # print the skewness
print("  skew ≈ 0: symmetric") # print the skewness
