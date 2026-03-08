# -------------------------------------------------
# File Name: 37_variance_of_random_variable.py
# Description: Computes random-variable variance via E[X^2]-E[X]^2 and relates to binomial variance.
# -------------------------------------------------

import numpy as np

# Var(X) = E[(X - E[X])^2] = E[X^2] - E[X]^2
x_vals = np.array([0, 1, 2, 3])
probs = np.array([0.1, 0.3, 0.4, 0.2])

e_x = np.sum(x_vals * probs)
e_x2 = np.sum(x_vals**2 * probs)
var_x = e_x2 - e_x**2

print("=== VARIANCE OF RANDOM VARIABLE ===")
print("Var(X) = E[X^2] - E[X]^2")
print()
print("x:", x_vals)
print("P(x):", probs)
print(f"E(X) = {e_x}")
print(f"E(X^2) = {e_x2}")
print(f"Var(X) = {var_x}")
print()
# Binomial Var(X) = n*p*(1-p)
n, p = 10, 0.5
print(f"Binomial(n={n}, p={p}): Var(X) = n*p*(1-p) = {n*p*(1-p)}")
