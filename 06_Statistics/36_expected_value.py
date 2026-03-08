# -------------------------------------------------
# File Name: 36_expected_value.py
# Description: Computes expected value E(X) for a discrete random variable and connects to binomial expectation.
# -------------------------------------------------

import numpy as np

# Discrete RV: E(X) = sum x_i * P(x_i)
x_vals = np.array([0, 1, 2, 3])
probs = np.array([0.1, 0.3, 0.4, 0.2])

e_x = np.sum(x_vals * probs)
print("=== EXPECTED VALUE E(X) ===")
print("Discrete: E(X) = Σ x_i * P(x_i)")
print()
print("x:", x_vals)
print("P(x):", probs)
print(f"E(X) = {e_x}")
print()
# Binomial E(X) = n*p
n, p = 10, 0.5
print(f"Binomial(n={n}, p={p}): E(X) = n*p = {n*p}")
