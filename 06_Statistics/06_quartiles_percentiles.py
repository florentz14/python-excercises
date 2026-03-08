# -------------------------------------------------
# File Name: 06_quartiles_percentiles.py
# Author: Florentino Báez
# Description: Computes quartiles, percentiles, and quantiles to describe positional statistics in a distribution.
# -------------------------------------------------

import numpy as np
# Standard library and NumPy implementations
import statistics  # Built-in descriptive stats
import numpy as np  # Fast numerical operations

data = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]) # Data set

print("=== DATA ===")
print(data) # Data set
print()

# Quartiles (Q1=25%, Q2=50%, Q3=75%)
q1, q2, q3 = np.percentile(data, [25, 50, 75]) # Quartiles
print("=== QUARTILES ===")
print(f"Q1 (25%): {q1}")
print(f"Q2 (50%, median): {q2}")
print(f"Q3 (75%): {q3}")
print()

# Percentiles
p90 = np.percentile(data, 90) # Percentiles
print("=== PERCENTILES ===")
print(f"90th percentile: {p90}")
print()

# Quantiles (0-1 scale)
quantiles = np.quantile(data, [0.25, 0.5, 0.75]) # Quantiles
print("=== np.quantile (0-1) ===")
print(f"[0.25, 0.5, 0.75]: {quantiles}")
print()

# statistics.quantiles (Python 3.8+)
quartiles_stat = statistics.quantiles(data, n=4) # Quartiles
print(f"statistics.quantiles(n=4): {quartiles_stat}")
