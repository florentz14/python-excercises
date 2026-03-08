# -------------------------------------------------
# File Name: 36_expected_value.py
# Description: Computes expected value E(X) for a discrete random variable and connects to binomial expectation.
# -------------------------------------------------

import numpy as np  # Numerical arrays and vectorized operations

# Discrete RV: E(X) = sum x_i * P(x_i)
x_vals = np.array([0, 1, 2, 3]) # x-values
probs = np.array([0.1, 0.3, 0.4, 0.2]) # probabilities

e_x = np.sum(x_vals * probs)  # Expected value E[X]
print("=== EXPECTED VALUE E(X) ===") # Expected value E(X)
print("Discrete: E(X) = Σ x_i * P(x_i)") # Discrete: E(X) = Σ x_i * P(x_i)
print()
print("x:", x_vals) # print the x-values
print("P(x):", probs) # print the probabilities
print(f"E(X) = {e_x}") # print the expected value E(X)
print()
# Binomial E(X) = n*p
n, p = 10, 0.5 # binomial parameters    
print(f"Binomial(n={n}, p={p}): E(X) = n*p = {n*p}") # print the binomial expected value E(X) = n*p
