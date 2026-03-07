# ------------------------------------------------------------
# File: 51_array_random.py
# Purpose: Random arrays with NumPy.
# Description: rand, randn, randint, shuffle, choice.
# ------------------------------------------------------------

import numpy as np

# Fix seed for reproducibility
np.random.seed(42)

# Uniform [0, 1): float
u = np.random.rand(3, 2)
print("rand(3, 2) uniform [0,1):\n", u)

# Standard normal (mean=0, std=1)
n = np.random.randn(4)
print("\nrandn(4) standard normal:", n)

# Random integers: [low, high) - high is exclusive
ints = np.random.randint(1, 11, size=(2, 5))
print("\nrandint(1, 11, (2,5)):\n", ints)

# Shuffle in place
v = np.array([1, 2, 3, 4, 5])
np.random.shuffle(v)
print("\nShuffled:", v)

# Random choice from array
choices = np.random.choice([10, 20, 30], size=5)
print("choice([10,20,30], 5):", choices)

# Choice with probabilities
weighted = np.random.choice([0, 1], size=10, p=[0.7, 0.3])
print("choice with p=[0.7,0.3]:", weighted)
