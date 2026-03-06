# ------------------------------------------------------------
# File: 40_vector_scalar_product.py
# Purpose: Multiply vector by scalar.
# Description: k * v = (k*v[0], k*v[1], ...).
# ------------------------------------------------------------

v = [2, -3, 5]
k = 3

# Each component multiplied by k
result = [k * x for x in v]
print("v =", v)
print("k =", k)
print("k * v =", result)
