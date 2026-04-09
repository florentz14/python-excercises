# -------------------------------------------------
# File Name: 100d_tridiagonal_operations.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: Sum, scalar multiply, efficient matrix-vector product.
# -------------------------------------------------

from matrix_helpers import TRIDIAG_5x5, print_matrix, print_vector, subtitle, title


def main() -> None:
    a_matrix = TRIDIAG_5x5
    title("4. OPERATIONS - Sum, scalar, matrix-vector product")
    n = len(a_matrix)

    b_matrix: list[list[float]] = [
        [1, 2, 0, 0, 0],
        [3, 1, 2, 0, 0],
        [0, 3, 1, 2, 0],
        [0, 0, 3, 1, 2],
        [0, 0, 0, 3, 1],
    ]

    subtitle("4a. Sum of two tridiagonal matrices")
    summed = [[a_matrix[i][j] + b_matrix[i][j] for j in range(n)] for i in range(n)]
    print_matrix(a_matrix, "Matrix A", fmt="5.1f")
    print_matrix(b_matrix, "Matrix B", fmt="5.1f")
    print_matrix(summed, "A + B (still tridiagonal)", fmt="5.1f")

    subtitle("4b. Scalar multiplication with k = 2")
    k = 2.0
    scaled = [[a_matrix[i][j] * k for j in range(n)] for i in range(n)]
    print_matrix(scaled, f"A x {k:.0f}", fmt="5.1f")

    subtitle("4c. Efficient matrix-vector product (use 3 diagonals)")
    x_vec = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(f"  Vector x: {x_vec}")

    y_standard = [sum(a_matrix[i][j] * x_vec[j] for j in range(n)) for i in range(n)]

    diag = [a_matrix[i][i] for i in range(n)]
    sup = [a_matrix[i][i + 1] for i in range(n - 1)]
    sub = [a_matrix[i + 1][i] for i in range(n - 1)]

    y_fast = [0.0] * n
    y_fast[0] = diag[0] * x_vec[0] + sup[0] * x_vec[1]
    for i in range(1, n - 1):
        y_fast[i] = sub[i - 1] * x_vec[i - 1] + diag[i] * x_vec[i] + sup[i] * x_vec[i + 1]
    y_fast[n - 1] = sub[n - 2] * x_vec[n - 2] + diag[n - 1] * x_vec[n - 1]

    print_vector(y_standard, "A*x (standard O(n^2))", label_width=22)
    print_vector(y_fast, "A*x (efficient O(n))", label_width=22)
    same = all(abs(left - right) < 1e-9 for left, right in zip(y_standard, y_fast))
    print(f"  Same results? {'YES' if same else 'NO'}")


if __name__ == "__main__":
    main()
