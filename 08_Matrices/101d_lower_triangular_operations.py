# -------------------------------------------------
# File Name: 101d_lower_triangular_operations.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: Sum, scalar multiply, L*L, transpose to upper.
# -------------------------------------------------

from matrix_helpers import LOWER_4x4, print_matrix, subtitle, title


def multiply_matrices(m1: list[list[float]], m2: list[list[float]], n: int) -> list[list[float]]:
    return [[sum(m1[i][k] * m2[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def main() -> None:
    a_matrix = LOWER_4x4
    title("4. OPERATIONS - Sum, scalar, multiply, transpose")
    n = len(a_matrix)

    b_matrix: list[list[float]] = [
        [3, 0, 0, 0],
        [1, 6, 0, 0],
        [5, 2, 4, 0],
        [8, 3, 1, 7],
    ]

    subtitle("4a. Sum of two lower triangular matrices")
    summed = [[a_matrix[i][j] + b_matrix[i][j] for j in range(n)] for i in range(n)]
    print_matrix(a_matrix, "Matrix A")
    print_matrix(b_matrix, "Matrix B")
    print_matrix(summed, "A + B (still lower triangular)")

    subtitle("4b. Scalar multiplication with k = 2")
    k = 2.0
    scaled = [[a_matrix[i][j] * k for j in range(n)] for i in range(n)]
    print_matrix(scaled, f"A x {k:.0f}")

    subtitle("4c. Product L*L (lower triangular remains lower)")
    product = multiply_matrices(a_matrix, b_matrix, n)
    print_matrix(product, "A x B (also lower triangular)")

    subtitle("4d. Transpose (becomes upper triangular)")
    transposed = [[a_matrix[j][i] for j in range(n)] for i in range(n)]
    print_matrix(transposed, "Transpose of A -> upper triangular")


if __name__ == "__main__":
    main()
