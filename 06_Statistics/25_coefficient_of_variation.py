# -------------------------------------------------
# File Name: 25_coefficient_of_variation.py
# Description: Computes coefficient of variation to compare relative variability across different scales.
# -------------------------------------------------

import numpy as np  # Numerical arrays and vectorized operations

data = np.array([12, 15, 18, 22, 25, 25, 28, 30, 33, 40]) # Data set
mean = np.mean(data) # Mean
std = np.std(data, ddof=1) # Standard deviation with Bessel's correction

print("=== DATA ===")
print(data) # print the data set
print()

# CV = std / mean (often as percentage)
cv = std / mean # Coefficient of variation
cv_pct = cv * 100 # Coefficient of variation percentage
print("=== COEFFICIENT OF VARIATION ===")
print(f"CV = std / mean = {cv:.4f}") # print the coefficient of variation
print(f"CV (%) = {cv_pct:.2f}%") # print the coefficient of variation percentage    
print()
print("Useful for comparing relative variability across different scales.")
