# -------------------------------------------------
# File Name: 02_median.py
# Author: Florentino Báez
# Description: Mediana (valor central).
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
