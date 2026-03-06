# ------------------------------------------------------------
# File: 24_matrix_transpose_division_negation.py
# Purpose: Transpose, scalar division, negation.
# Description: G^T, A÷k, -A.
# ------------------------------------------------------------


def print_matrix(matrix, name="Matrix"):
    """Print matrix with aligned columns."""
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


# Transpose
G = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print_matrix(G, "G (3x4)")
transposed = [[G[i][j] for i in range(len(G))] for j in range(len(G[0]))]
print_matrix(transposed, "G^T (4x3)")

# Division by scalar
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 2
divided = [[x / k for x in row] for row in A]
print_matrix(A, "A")
print_matrix(divided, f"A ÷ {k}")

# Negation
negated = [[-x for x in row] for row in A]
print_matrix(negated, "-A")
