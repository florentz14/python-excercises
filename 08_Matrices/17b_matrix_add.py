# -------------------------------------------------
# File Name: 17b_matrix_add.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Add two matrices of the same shape.
# -------------------------------------------------

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
sum_ab = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print("A + B:")
for row in sum_ab:
    print(row)
