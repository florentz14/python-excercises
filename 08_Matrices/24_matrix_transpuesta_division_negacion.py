"""
08_Matrices - Transpuesta, división por escalar y negación
===========================================================
Ejemplos 6-8: G^T, A÷k, -A.
"""


def print_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


# Transpuesta
G = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print_matrix(G, "G (3x4)")
transpuesta = [[G[i][j] for i in range(len(G))] for j in range(len(G[0]))]
print_matrix(transpuesta, "G^T (4x3)")

# División por escalar
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 2
div_result = [[x / k for x in row] for row in A]
print_matrix(A, "A")
print_matrix(div_result, f"A ÷ {k}")

# Negación
negacion = [[-x for x in row] for row in A]
print_matrix(negacion, "-A")
