# -------------------------------------------------
# File Name: 10_uniform_distribution.py
# Author: Florentino Báez
# Description: Distribución uniforme.
# -------------------------------------------------

import numpy as np

low, high = 0, 1
uniform_samples = np.random.uniform(low, high, 100)

print("=== UNIFORM [0, 1] ===")
print(f"Sample mean: {np.mean(uniform_samples):.4f} (expected 0.5)")
