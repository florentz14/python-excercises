"""
08_Matrices - Multiplicación de matrices y producto de Hadamard (elemento a elemento)
=====================================================================================
Ejemplos 4-5: C×D (producto matricial), E⊙F (Hadamard).
"""


def print_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


# Multiplicación matricial C (3x2) × D (2x3)
C = [[1, 2], [3, 4], [5, 6]]
D = [[7, 8, 9], [10, 11, 12]]
print_matrix(C, "C (3x2)")
print_matrix(D, "D (2x3)")

result = []
for i in range(len(C)):
    row = []
    for j in range(len(D[0])):
        s = sum(C[i][k] * D[k][j] for k in range(len(D)))
        row.append(s)
    result.append(row)
print_matrix(result, "C x D (3x3)")

# Producto de Hadamard (elemento a elemento)
E = [[1, 2, 3], [4, 5, 6]]
F = [[2, 3, 4], [5, 6, 7]]
print_matrix(E, "E")
print_matrix(F, "F")
hadamard = [[E[i][j] * F[i][j] for j in range(len(E[0]))] for i in range(len(E))]
print_matrix(hadamard, "E ⊙ F (Hadamard)")
