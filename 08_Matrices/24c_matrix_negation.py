# -------------------------------------------------
# File Name: 24c_matrix_negation.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Negate every entry (-A).
# -------------------------------------------------

def print_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix(A, "A")
negated = [[-x for x in row] for row in A]
print_matrix(negated, "-A")
