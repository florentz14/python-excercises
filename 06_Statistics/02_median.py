# -------------------------------------------------
# File Name: 02_median.py
# Author: Florentino Báez
# Description: Computes the median (central value) and shows equivalent calculations with statistics and NumPy.
# -------------------------------------------------

import statistics
import numpy as np

data = [12, 15, 18, 22, 25, 25, 28, 30, 33, 40]

print("=== DATA ===")
print(data)
print()

# Median
median = statistics.median(data)
print(f"Median (middle value): {median}")
print()

# NumPy
print("=== NUMPY ===")
print(f"np.median: {np.median(data):.2f}")
