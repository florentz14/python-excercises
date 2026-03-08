# -------------------------------------------------
# File Name: 02_median.py
# Author: Florentino Báez
# Description: Computes the median (central value) and shows equivalent calculations with statistics and NumPy.
# -------------------------------------------------

# Standard library and NumPy implementations
import statistics  # Built-in descriptive stats
import numpy as np  # Fast numerical operations

data = [12, 15, 18, 22, 25, 25, 28, 30, 33, 40]  # Sorted sample for clarity

print("=== DATA ===")
print(data)  # Original values
print()

# Middle value (or average of two middle values)
median = statistics.median(data)
print(f"Median (middle value): {median}")
print()

# Same metric computed with NumPy
print("=== NUMPY ===")
print(f"np.median: {np.median(data):.2f}")
