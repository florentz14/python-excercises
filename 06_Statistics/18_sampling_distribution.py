# -------------------------------------------------
# File Name: 18_sampling_distribution.py
# Author: Florentino Báez
# Description: Simulates many samples to build the sampling distribution of the mean and estimate standard error.
# -------------------------------------------------

import numpy as np # Fast numerical operations

np.random.seed(42)
population = np.random.normal(100, 15, 10_000) # Population

n = 30 # Sample size
n_samples = 1000 # Number of samples
sample_means = [np.random.choice(population, n).mean() for _ in range(n_samples)] # Sample means

print("=== POPULATION ===")
print(f"Mean: {np.mean(population):.2f}, Std: {np.std(population):.2f}") # Mean and standard deviation of the population
print()

print("=== SAMPLING DISTRIBUTION OF MEAN (1000 samples, n=30 each) ===")
print(f"Mean of sample means: {np.mean(sample_means):.2f}") # Mean of the sample means
print(f"Std of sample means (SE): {np.std(sample_means):.2f}") # Standard deviation of the sample means
print(f"Expected SE = pop_std/sqrt(n): {np.std(population)/np.sqrt(n):.2f}") # Expected standard error  
