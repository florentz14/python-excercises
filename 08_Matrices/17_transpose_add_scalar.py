# ------------------------------------------------------------
# File: 17_transpose_add_scalar.py
# Purpose: Transpose, add matrices, scalar product.
# Description: A^T, A+B, k*A with list comprehensions.
# ------------------------------------------------------------

# Transpose
original = [[1, 2, 3], [4, 5, 6]]
print("Original (2x3):")
for row in original:
    print(row)

transposed = [
    [original[i][j] for i in range(len(original))]
    for j in range(len(original[0]))
]
print("Transpose (3x2):")
for row in transposed:
    print(row)

# Add matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
sum_ab = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print("\nA + B:")
for row in sum_ab:
    print(row)

# Scalar product
k = 2
M = [[1, 2], [3, 4]]
scaled = [[x * k for x in row] for row in M]
print(f"\n{k} * M:")
for row in scaled:
    print(row)
