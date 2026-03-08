# -------------------------------------------------
# File Name: 17_random_sample.py
# Author: Florentino Báez
# Description: Muestreo aleatorio simple y con reemplazo.
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

# With replacement
sample_wr = np.random.choice(population, size=n, replace=True)
print("=== SAMPLE WITH REPLACEMENT ===")
print(f"Mean: {np.mean(sample_wr):.2f}")
