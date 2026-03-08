# -------------------------------------------------
# File Name: 27_kurtosis.py
# Description: Computes excess kurtosis to assess tail heaviness and outlier-proneness relative to normal.
# -------------------------------------------------

import numpy as np  # Numerical arrays and vectorized operations
from scipy import stats  # Statistical tests and probability distributions

data = np.array([12, 15, 18, 22, 25, 25, 28, 30, 33, 40]) # Data set

print("=== DATA ===")
print(data)
print()

# Kurtosis (Fisher definition; excess kurtosis)
kurt = stats.kurtosis(data)
print("=== KURTOSIS (excess) ===")
print(f"Kurtosis: {kurt:.4f}") # print the kurtosis
print("  kurt > 0: heavy tails (leptokurtic)")
print("  kurt < 0: light tails (platykurtic)") # print the kurtosis
print("  kurt ≈ 0: similar to normal (mesokurtic)") # print the kurtosis
