# ------------------------------------------------------------
# File: 22_add_subtract_scalar.py
# Purpose: Add, subtract, scalar product with formatting.
# Description: A+B, A-B, k*A with aligned print.
# ------------------------------------------------------------


def print_matrix(matrix, name="Matrix"):
    """Print matrix with aligned columns."""
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print_matrix(A, "A")
print_matrix(B, "B")

# Add
sum_ab = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print_matrix(sum_ab, "A + B")

# Subtract
diff = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print_matrix(diff, "A - B")

# Scalar
k = 2
scaled = [[x * k for x in row] for row in A]
print_matrix(scaled, f"A × {k}")
