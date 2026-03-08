# -------------------------------------------------
# File Name: 10_add.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: A + B requires same shape; result[i][j] = A[i][j] + B[i][j].
# -------------------------------------------------

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

rows, cols = len(A), len(A[0])
# Element-wise addition
sum_matrix = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]

print("A =", A)
print("B =", B)
print("A + B =", sum_matrix)
