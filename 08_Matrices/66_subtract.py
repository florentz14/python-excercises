# -------------------------------------------------
# File Name: 66_subtract.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: v - w = (v[0]-w[0], v[1]-w[1], ...).
# -------------------------------------------------

v = [5, 7, 2]
w = [1, 3, 4]

# Component-wise subtraction
diff = [v[i] - w[i] for i in range(len(v))]
print("v =", v)
print("w =", w)
print("v - w =", diff)
