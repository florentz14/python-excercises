# -------------------------------------------------
# File Name: 16_standardization.py
# Author: Florentino Báez
# Description: Estandarización (mean=0, std=1).
# -------------------------------------------------

import numpy as np

data = np.array([10, 12, 14, 15, 16, 18, 20, 100])

print("=== DATA ===")
print(data)
print()

# Standardization
mean = np.mean(data)
std = np.std(data, ddof=1)
standardized = (data - mean) / std

print("=== STANDARDIZED DATA ===")
print(standardized)
print(f"Mean: {np.mean(standardized):.4f}, Std: {np.std(standardized, ddof=1):.4f}")
