# ------------------------------------------------------------
# File: 39_vector_add.py
# Purpose: Add two vectors component-wise.
# Description: v + w = (v[0]+w[0], v[1]+w[1], ...).
# ------------------------------------------------------------

v = [1, 2, 3]
w = [4, 5, 6]

# Component-wise addition
sum_vw = [v[i] + w[i] for i in range(len(v))]
print("v =", v)
print("w =", w)
print("v + w =", sum_vw)
