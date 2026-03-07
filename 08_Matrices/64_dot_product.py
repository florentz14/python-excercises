# ------------------------------------------------------------
# File: 41_vector_dot_product.py
# Purpose: Dot product (scalar product).
# Description: v·w = v[0]*w[0] + v[1]*w[1] + ... (result is scalar).
# ------------------------------------------------------------

v = [1, 2, 3]
w = [4, 5, 6]

# Dot product: sum of component-wise products
dot = sum(v[i] * w[i] for i in range(len(v)))
print("v =", v)
print("w =", w)
print("v · w =", dot)
