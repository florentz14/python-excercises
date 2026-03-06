# ------------------------------------------------------------
# File: 25_matrix_identity_trace_determinant.py
# Purpose: Identity × matrix, trace, 2×2 determinant.
# Description: H×I = H, trace = sum of diagonal, det for 2x2.
# ------------------------------------------------------------


def print_matrix(matrix, name="Matrix"):
    """Print matrix with aligned columns."""
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


# Identity × matrix: H × I = H
I = [[1, 0], [0, 1]]
H = [[5, 6], [7, 8]]
print_matrix(I, "I (2x2)")
print_matrix(H, "H")
result = [[sum(H[i][k] * I[k][j] for k in range(len(I))) for j in range(len(I[0]))] for i in range(len(H))]
print_matrix(result, "H × I")

# Trace = sum of main diagonal
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix(M, "Square matrix")
trace = sum(M[i][i] for i in range(len(M)))
print(f"Trace (diagonal sum): {trace}\n")

# Determinant 2x2: ad - bc
M2 = [[4, 7], [2, 6]]
print_matrix(M2, "2x2 matrix")
det = M2[0][0] * M2[1][1] - M2[0][1] * M2[1][0]
print(f"Determinant = (4×6) - (7×2) = {det}")
