# -------------------------------------------------
# File Name: 27_kurtosis.py
# Description: Computes excess kurtosis to assess tail heaviness and outlier-proneness relative to normal.
# -------------------------------------------------

import numpy as np
from scipy import stats

data = np.array([12, 15, 18, 22, 25, 25, 28, 30, 33, 40])

print("=== DATA ===")
print(data)
print()

# Kurtosis (Fisher definition; excess kurtosis)
kurt = stats.kurtosis(data)
print("=== KURTOSIS (excess) ===")
print(f"Kurtosis: {kurt:.4f}")
print("  kurt > 0: heavy tails (leptokurtic)")
print("  kurt < 0: light tails (platykurtic)")
print("  kurt ≈ 0: similar to normal (mesokurtic)")
