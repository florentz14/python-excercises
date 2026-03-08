# -------------------------------------------------
# File Name: 09_normal_distribution.py
# Author: Florentino Báez
# Description: Distribución normal.
# -------------------------------------------------

import numpy as np
from scipy import stats

mean, std = 100, 15
x = 115
z = (x - mean) / std
prob_below = stats.norm.cdf(z)

print("=== NORMAL DISTRIBUTION (mean=100, std=15) ===")
print(f"P(X <= 115): {prob_below:.4f}")
print(f"P(X > 115): {1 - prob_below:.4f}")
print()

# Generate random samples
samples = np.random.normal(mean, std, 1000)
print(f"Sample mean: {np.mean(samples):.2f}, sample std: {np.std(samples):.2f}")
print()

# PDF and CDF
print("=== PDF / CDF ===")
print(f"norm.pdf(100, 100, 15): {stats.norm.pdf(100, 100, 15):.4f}")
print(f"norm.cdf(115, 100, 15): {stats.norm.cdf(115, 100, 15):.4f}")
