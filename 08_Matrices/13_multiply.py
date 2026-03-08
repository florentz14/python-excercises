# -------------------------------------------------
# File Name: 13_multiply.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: A(m×n) * B(n×p) = C(m×p). C[i][j] = sum_k A[i][k]*B[k][j].
# -------------------------------------------------

A = [[1, 2], [3, 4]]  # 2x2
B = [[5, 6], [7, 8]]  # 2x2

# C[i][j] = sum over k of A[i][k] * B[k][j]
m, n, p = len(A), len(A[0]), len(B[0])
C = [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(p)] for i in range(m)]

print("A =", A)
print("B =", B)
print("A * B =", C)
