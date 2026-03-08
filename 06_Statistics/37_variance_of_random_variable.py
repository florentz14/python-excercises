# -------------------------------------------------
# File Name: 37_variance_of_random_variable.py
# Description: Computes random-variable variance via E[X^2]-E[X]^2 and relates to binomial variance.
# -------------------------------------------------

import numpy as np  # Numerical arrays and vectorized operations

# Var(X) = E[(X - E[X])^2] = E[X^2] - E[X]^2
x_vals = np.array([0, 1, 2, 3]) # x-values
probs = np.array([0.1, 0.3, 0.4, 0.2]) # probabilities

e_x = np.sum(x_vals * probs)  # Expected value E[X]
e_x2 = np.sum(x_vals**2 * probs)  # Expected value E[X^2]
var_x = e_x2 - e_x**2  # Variance Var(X)

print("=== VARIANCE OF RANDOM VARIABLE ===")
print("Var(X) = E[X^2] - E[X]^2") # Var(X) = E[X^2] - E[X]^2
print()
print("x:", x_vals) # print the x-values
print("P(x):", probs)
print(f"E(X) = {e_x}") # print the expected value E(X)
print(f"E(X^2) = {e_x2}") # print the expected value E(X^2)
print(f"Var(X) = {var_x}") # print the variance Var(X)
print()
# Binomial Var(X) = n*p*(1-p)
n, p = 10, 0.5
print(f"Binomial(n={n}, p={p}): Var(X) = n*p*(1-p) = {n*p*(1-p)}")
