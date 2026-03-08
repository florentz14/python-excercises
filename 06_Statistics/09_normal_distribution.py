# -------------------------------------------------
# File Name: 09_normal_distribution.py
# Author: Florentino Báez
# Description: Evaluates normal-distribution probabilities (CDF/tails) and generates samples for empirical checks.
# -------------------------------------------------

# Standard library and NumPy implementations
import numpy as np  # Fast numerical operations
from scipy import stats

mean, std = 100, 15 # Mean and standard deviation
x = 115 # Value
z = (x - mean) / std # Z-score
prob_below = stats.norm.cdf(z) # Probability below x

print("=== NORMAL DISTRIBUTION (mean=100, std=15) ===")
print(f"P(X <= 115): {prob_below:.4f}") # Probability below x
print(f"P(X > 115): {1 - prob_below:.4f}")
print()

# Generate random samples
samples = np.random.normal(mean, std, 1000) # Random samples
print(f"Sample mean: {np.mean(samples):.2f}, sample std: {np.std(samples):.2f}")
print()

# PDF and CDF
print("=== PDF / CDF ===")
print(f"norm.pdf(100, 100, 15): {stats.norm.pdf(100, 100, 15):.4f}") # PDF
print(f"norm.cdf(115, 100, 15): {stats.norm.cdf(115, 100, 15):.4f}") # CDF
