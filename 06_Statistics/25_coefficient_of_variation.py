# -------------------------------------------------
# File Name: 25_coefficient_of_variation.py
# Description: Computes coefficient of variation to compare relative variability across different scales.
# -------------------------------------------------

import numpy as np

data = np.array([12, 15, 18, 22, 25, 25, 28, 30, 33, 40])
mean = np.mean(data)
std = np.std(data, ddof=1)

print("=== DATA ===")
print(data)
print()

# CV = std / mean (often as percentage)
cv = std / mean
cv_pct = cv * 100
print("=== COEFFICIENT OF VARIATION ===")
print(f"CV = std / mean = {cv:.4f}")
print(f"CV (%) = {cv_pct:.2f}%")
print()
print("Useful for comparing relative variability across different scales.")
