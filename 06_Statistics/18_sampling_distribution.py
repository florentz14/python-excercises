# -------------------------------------------------
# File Name: 18_sampling_distribution.py
# Author: Florentino Báez
# Description: Simulates many samples to build the sampling distribution of the mean and estimate standard error.
# -------------------------------------------------

import numpy as np

np.random.seed(42)
population = np.random.normal(100, 15, 10_000)

n = 30
n_samples = 1000
sample_means = [np.random.choice(population, n).mean() for _ in range(n_samples)]

print("=== POPULATION ===")
print(f"Mean: {np.mean(population):.2f}, Std: {np.std(population):.2f}")
print()

print("=== SAMPLING DISTRIBUTION OF MEAN (1000 samples, n=30 each) ===")
print(f"Mean of sample means: {np.mean(sample_means):.2f}")
print(f"Std of sample means (SE): {np.std(sample_means):.2f}")
print(f"Expected SE = pop_std/sqrt(n): {np.std(population)/np.sqrt(n):.2f}")
