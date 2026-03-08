# -------------------------------------------------
# File Name: 24_range.py
# Description: Rango (max - min).
# -------------------------------------------------

import numpy as np

data = np.array([12, 15, 18, 22, 25, 25, 28, 30, 33, 40])

print("=== DATA ===")
print(data)
print()

# Range = max - min
r = np.max(data) - np.min(data)
print("=== RANGE ===")
print(f"Min: {np.min(data)}, Max: {np.max(data)}")
print(f"Range = max - min = {r}")
