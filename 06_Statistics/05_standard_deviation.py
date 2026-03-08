# -------------------------------------------------
# File Name: 05_standard_deviation.py
# Author: Florentino Báez
# Description: Desviación estándar (población y muestra).
# -------------------------------------------------

import statistics
import numpy as np

data = [12, 15, 18, 22, 25, 25, 28, 30, 33, 40]

print("=== DATA ===")
print(data)
print()

# Standard deviation
std_p = statistics.pstdev(data)
std_s = statistics.stdev(data)
print(f"Std dev (population): {std_p:.2f}")
print(f"Std dev (sample): {std_s:.2f}")
print()

# NumPy
print("=== NUMPY ===")
print(f"np.std (ddof=0): {np.std(data):.2f}")
print(f"np.std (ddof=1, sample): {np.std(data, ddof=1):.2f}")
