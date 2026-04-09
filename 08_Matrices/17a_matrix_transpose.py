# -------------------------------------------------
# File Name: 17a_matrix_transpose.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Transpose with nested list comprehensions.
# -------------------------------------------------

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
