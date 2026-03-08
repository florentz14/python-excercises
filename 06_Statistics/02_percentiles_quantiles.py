# -------------------------------------------------
# File Name: 02_percentiles_quantiles.py
# Author: Florentino Báez
# Date: Statistics
# Description: Percentiles, quantiles, IQR, quartiles.
# -------------------------------------------------

import numpy as np
import statistics

data = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])

print("=== DATA ===")
print(data)
print()

# Quartiles (Q1=25%, Q2=50%, Q3=75%)
q1, q2, q3 = np.percentile(data, [25, 50, 75])
print("=== QUARTILES ===")
print(f"Q1 (25%): {q1}")
print(f"Q2 (50%, median): {q2}")
print(f"Q3 (75%): {q3}")
print()

# IQR (Interquartile Range)
iqr = q3 - q1
print(f"IQR = Q3 - Q1 = {iqr}")
print()

# Percentiles
p90 = np.percentile(data, 90)
print("=== PERCENTILES ===")
print(f"90th percentile: {p90}")
print(f"np.percentile(data, 90) = {np.percentile(data, 90)}")
print()

# Quantiles (0-1 scale)
quantiles = np.quantile(data, [0.25, 0.5, 0.75])
print("=== np.quantile (0-1) ===")
print(f"[0.25, 0.5, 0.75]: {quantiles}")
print()

# Five-number summary
print("=== FIVE-NUMBER SUMMARY ===")
print(f"Min: {np.min(data)}")
print(f"Q1: {q1}")
print(f"Median: {q2}")
print(f"Q3: {q3}")
print(f"Max: {np.max(data)}")
print()

# statistics.quantiles (Python 3.8+)
quartiles_stat = statistics.quantiles(data, n=4)
print(f"statistics.quantiles(n=4): {quartiles_stat}")
