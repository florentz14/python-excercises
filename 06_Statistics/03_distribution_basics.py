# -------------------------------------------------
# File Name: 03_distribution_basics.py
# Author: Florentino Báez
# Date: Statistics
# Description: Probability basics, normal and other distributions.
# -------------------------------------------------

import numpy as np
from scipy import stats

# --- Probability basics ---
# P(A) = favorable / total
favorable = 3
total = 10
prob = favorable / total
print("=== PROBABILITY BASICS ===")
print(f"P(A) = favorable/total = {favorable}/{total} = {prob}")
print()

# --- Normal distribution ---
mean, std = 100, 15
x = 115
z = (x - mean) / std
prob_below = stats.norm.cdf(z)
print("=== NORMAL DISTRIBUTION (mean=100, std=15) ===")
print(f"P(X <= 115): {prob_below:.4f}")
print(f"P(X > 115): {1 - prob_below:.4f}")
print()

# Generate random samples from normal
samples = np.random.normal(mean, std, 1000)
print(f"Sample mean: {np.mean(samples):.2f}, sample std: {np.std(samples):.2f}")
print()

# PDF and CDF
print("=== PDF / CDF ===")
print(f"norm.pdf(100, 100, 15): {stats.norm.pdf(100, 100, 15):.4f}")
print(f"norm.cdf(115, 100, 15): {stats.norm.cdf(115, 100, 15):.4f}")
print()

# --- Uniform distribution ---
low, high = 0, 1
uniform_samples = np.random.uniform(low, high, 100)
print("=== UNIFORM [0, 1] ===")
print(f"Sample mean: {np.mean(uniform_samples):.4f} (expected 0.5)")
print()

# --- Binomial (n trials, p success) ---
n, p = 10, 0.5
binom_probs = [stats.binom.pmf(k, n, p) for k in range(n + 1)]
print("=== BINOMIAL (n=10, p=0.5) ===")
print(f"P(k=5): {stats.binom.pmf(5, n, p):.4f}")
print(f"P(k <= 5): {stats.binom.cdf(5, n, p):.4f}")
