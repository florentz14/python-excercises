# -------------------------------------------------
# File Name: 24b_matrix_scalar_divide.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Divide each matrix entry by a scalar.
# -------------------------------------------------

def print_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 2
divided = [[x / k for x in row] for row in A]
print_matrix(A, "A")
print_matrix(divided, f"A / {k}")
