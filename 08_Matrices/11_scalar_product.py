# -------------------------------------------------
# File Name: 11_scalar_product.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: k*A: each element multiplied by k.
# -------------------------------------------------

A = [[1, 2], [3, 4]]
k = 3

# Each element: k * A[i][j]
result = [[k * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

print("A =", A)
print("k =", k)
print("k * A =", result)
