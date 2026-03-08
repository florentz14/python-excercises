# -------------------------------------------------
# File Name: 17_random_sample.py
# Author: Florentino Báez
# Description: Draws simple random samples with and without replacement and compares sample/population metrics.
# -------------------------------------------------

import numpy as np # Fast numerical operations

np.random.seed(42)
population = np.random.normal(100, 15, 10_000) # Population

print("=== POPULATION ===")
print(f"Size: {len(population)}") # Size of the population
print(f"Mean: {np.mean(population):.2f}, Std: {np.std(population):.2f}")
print()

# Simple random sample
n = 30
sample = np.random.choice(population, size=n, replace=False) # Simple random sample
print("=== SIMPLE RANDOM SAMPLE (n=30) ===")
print(f"Sample mean: {np.mean(sample):.2f}") # Sample mean of the simple random sample
print(f"Sample std: {np.std(sample, ddof=1):.2f}") # Sample standard deviation of the simple random sample
print()

# With replacement
sample_wr = np.random.choice(population, size=n, replace=True) # Sample with replacement
print("=== SAMPLE WITH REPLACEMENT ===")
print(f"Mean: {np.mean(sample_wr):.2f}") # Sample mean of the sample with replacement
print(f"Sample std: {np.std(sample_wr, ddof=1):.2f}") # Sample standard deviation of the sample with replacement
print()

# Comparison
print("=== COMPARISON ===")
print(f"Simple random sample mean: {np.mean(sample):.2f}, Sample std: {np.std(sample, ddof=1):.2f}")
print(f"Sample with replacement mean: {np.mean(sample_wr):.2f}, Sample std: {np.std(sample_wr, ddof=1):.2f}")