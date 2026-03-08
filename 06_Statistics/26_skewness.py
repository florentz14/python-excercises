# -------------------------------------------------
# File Name: 26_skewness.py
# Description: Computes skewness to assess distribution asymmetry (left- or right-tailed).
# -------------------------------------------------

import numpy as np
from scipy import stats

data = np.array([12, 15, 18, 22, 25, 25, 28, 30, 33, 40])

print("=== DATA ===")
print(data)
print()

# Skewness
skew = stats.skew(data)
print("=== SKEWNESS ===")
print(f"Skewness: {skew:.4f}")
print("  skew > 0: right-tailed (positive skew)")
print("  skew < 0: left-tailed (negative skew)")
print("  skew ≈ 0: symmetric")
