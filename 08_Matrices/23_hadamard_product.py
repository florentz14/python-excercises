# -------------------------------------------------
# File Name: 23_hadamard_product.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: C×D (matrix product), E⊙F (element-wise Hadamard).
# -------------------------------------------------

def print_matrix(matrix, name="Matrix"):
    """Print matrix with aligned columns."""
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


# Matrix product: C (3x2) × D (2x3)
C = [[1, 2], [3, 4], [5, 6]]
D = [[7, 8, 9], [10, 11, 12]]
print_matrix(C, "C (3x2)")
print_matrix(D, "D (2x3)")

result = []
for i in range(len(C)):
    row = [sum(C[i][k] * D[k][j] for k in range(len(D))) for j in range(len(D[0]))]
    result.append(row)
print_matrix(result, "C × D (3x3)")

# Hadamard: element-wise product E⊙F
E = [[1, 2, 3], [4, 5, 6]]
F = [[2, 3, 4], [5, 6, 7]]
print_matrix(E, "E")
print_matrix(F, "F")
hadamard = [[E[i][j] * F[i][j] for j in range(len(E[0]))] for i in range(len(E))]
print_matrix(hadamard, "E ⊙ F (Hadamard)")
