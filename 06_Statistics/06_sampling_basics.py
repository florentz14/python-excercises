# -------------------------------------------------
# File Name: 06_sampling_basics.py
# Author: Florentino Báez
# Date: Statistics
# Description: Sampling, random sample, sampling distribution.
# -------------------------------------------------

import numpy as np

np.random.seed(42)
population = np.random.normal(100, 15, 10_000)

print("=== POPULATION ===")
print(f"Size: {len(population)}")
print(f"Mean: {np.mean(population):.2f}, Std: {np.std(population):.2f}")
print()

# Simple random sample
n = 30
sample = np.random.choice(population, size=n, replace=False)
print("=== SIMPLE RANDOM SAMPLE (n=30) ===")
print(f"Sample mean: {np.mean(sample):.2f}")
print(f"Sample std: {np.std(sample, ddof=1):.2f}")
print()

# Multiple samples -> sampling distribution of the mean
n_samples = 1000
sample_means = [np.random.choice(population, n).mean() for _ in range(n_samples)]

print("=== SAMPLING DISTRIBUTION OF MEAN (1000 samples, n=30 each) ===")
print(f"Mean of sample means: {np.mean(sample_means):.2f}")
print(f"Std of sample means (SE): {np.std(sample_means):.2f}")
print(f"Expected SE = pop_std/sqrt(n): {np.std(population)/np.sqrt(n):.2f}")
print()

# With replacement
sample_wr = np.random.choice(population, size=n, replace=True)
print("=== SAMPLE WITH REPLACEMENT ===")
print(f"Mean: {np.mean(sample_wr):.2f}")
print()

# Systematic sampling (every k-th element)
k = len(population) // 50
systematic = population[::k][:50]
print("=== SYSTEMATIC SAMPLE (every k-th) ===")
print(f"Size: {len(systematic)}, Mean: {np.mean(systematic):.2f}")
