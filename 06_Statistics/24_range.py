# -------------------------------------------------
# File Name: 24_range.py
# Description: Computes the range (max-min) as a quick measure of total spread.
# -------------------------------------------------

import numpy as np  # Numerical arrays and vectorized operations

data = np.array([12, 15, 18, 22, 25, 25, 28, 30, 33, 40]) # Data set

print("=== DATA ===")
print(data) # print the data set
print()

# Range = max - min
r = np.max(data) - np.min(data) # Range = max - min
print("=== RANGE ===")
print(f"Min: {np.min(data)}, Max: {np.max(data)}") # print the minimum and maximum values
print(f"Range = max - min = {r}") # print the range
