# -------------------------------------------------
# File Name: 19_systematic_sampling.py
# Author: Florentino Báez
# Description: Implements systematic sampling by selecting every k-th element from a population.
# -------------------------------------------------

import numpy as np # Fast numerical operations  

np.random.seed(42) # Seed for reproducibility
population = np.random.normal(100, 15, 10_000) # Population

k = len(population) // 50 # Step size
systematic = population[::k][:50] # Systematic sample

print("=== SYSTEMATIC SAMPLE (every k-th) ===")
print(f"Size: {len(systematic)}, Mean: {np.mean(systematic):.2f}") # Size and mean of the systematic sample (every k-th element)
