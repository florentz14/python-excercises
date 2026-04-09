# -------------------------------------------------
# File Name: 102d_upper_triangular_operations.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: Sum, scalar multiply, transpose to lower.
# -------------------------------------------------

from matrix_helpers import UPPER_4x4, print_matrix, subtitle, title


def main() -> None:
    a_matrix = UPPER_4x4
    title("4. OPERATIONS - Sum, transpose, scalar multiplication")
    n = len(a_matrix)

    b_matrix: list[list[float]] = [
        [2, 1, 0, 3],
        [0, 4, 5, 2],
        [0, 0, 1, 6],
        [0, 0, 0, 7],
    ]

    subtitle("4a. Sum of two upper triangular matrices")
    summed = [[a_matrix[i][j] + b_matrix[i][j] for j in range(n)] for i in range(n)]
    print_matrix(a_matrix, "Matrix A")
    print_matrix(b_matrix, "Matrix B")
    print_matrix(summed, "A + B (still upper triangular)")

    subtitle("4b. Scalar multiplication")
    k = 3.0
    scaled = [[a_matrix[i][j] * k for j in range(n)] for i in range(n)]
    print_matrix(scaled, f"A x {k:.0f}")

    subtitle("4c. Transpose (becomes lower triangular)")
    transposed = [[a_matrix[j][i] for j in range(n)] for i in range(n)]
    print_matrix(transposed, "Transpose of A -> lower triangular")


if __name__ == "__main__":
    main()
