# -------------------------------------------------
# File Name: 19_systematic_sampling.py
# Author: Florentino Báez
# Description: Implements systematic sampling by selecting every k-th element from a population.
# -------------------------------------------------

import numpy as np

np.random.seed(42)
population = np.random.normal(100, 15, 10_000)

k = len(population) // 50
systematic = population[::k][:50]

print("=== SYSTEMATIC SAMPLE (every k-th) ===")
print(f"Size: {len(systematic)}, Mean: {np.mean(systematic):.2f}")
