# ------------------------------------------------------------
# File: 12_matrix_transpose.py
# Purpose: Transpose a matrix (swap rows and columns).
# Description: A^T: row j of A^T = column j of A. If A is m×n, A^T is n×m.
# ------------------------------------------------------------

A = [
    [1, 2, 3],
    [4, 5, 6],
]

# Transpose: A^T[i][j] = A[j][i]
rows, cols = len(A), len(A[0])
transposed = [[A[i][j] for i in range(rows)] for j in range(cols)]

print("A =")
for row in A:
    print(" ", row)
print("A^T (transpose) =")
for row in transposed:
    print(" ", row)
