# -------------------------------------------------
# File Name: 24a_matrix_transpose.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Transpose of a rectangular matrix.
# -------------------------------------------------

def print_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


G = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print_matrix(G, "G (3x4)")
transposed = [[G[i][j] for i in range(len(G))] for j in range(len(G[0]))]
print_matrix(transposed, "G^T (4x3)")
