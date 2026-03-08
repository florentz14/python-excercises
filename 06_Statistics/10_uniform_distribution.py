# -------------------------------------------------
# File Name: 10_uniform_distribution.py
# Author: Florentino Báez
# Description: Generates uniform random samples and checks expected behavior using sample statistics.
# -------------------------------------------------

import numpy as np # Fast numerical operations

low, high = 0, 1 # Low and high
uniform_samples = np.random.uniform(low, high, 100) # Uniform samples

print("=== UNIFORM [0, 1] ===")
print(f"Sample mean: {np.mean(uniform_samples):.4f} (expected 0.5)")
