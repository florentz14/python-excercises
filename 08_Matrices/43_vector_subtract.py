# ------------------------------------------------------------
# File: 43_vector_subtract.py
# Purpose: Subtract two vectors component-wise.
# Description: v - w = (v[0]-w[0], v[1]-w[1], ...).
# ------------------------------------------------------------

v = [5, 7, 2]
w = [1, 3, 4]

# Component-wise subtraction
diff = [v[i] - w[i] for i in range(len(v))]
print("v =", v)
print("w =", w)
print("v - w =", diff)
