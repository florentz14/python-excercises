# -------------------------------------------------
# File Name: 106_standard_matrix_multiplication.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Standard matrix multiplication using dot product.
# -------------------------------------------------

"""
Standard matrix multiplication (dot product).
Number of columns in A must equal number of rows in B.
"""

SEPARATOR = "=" * 40


def multiply_matrices(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """
    Perform standard matrix multiplication (dot product).
    Number of columns in A must equal number of rows in B.
    Result dimensions: (rows_A x cols_B)
    """
    if not a or not b or not a[0] or not b[0]:
        raise ValueError("Matrices must be non-empty.")

    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
        raise ValueError(
            f"Cannot multiply: columns in A ({cols_a}) "
            f"must equal rows in B ({rows_b})."
        )

    result = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]

    return result


def print_matrix(matrix: list[list[float]], name: str = "Matrix") -> None:
    """Print a matrix in a readable format."""
    print(f"\n{name}:")
    for row in matrix:
        print("  ", row)


if __name__ == "__main__":
    matrix_a = [
        [1, 2, 3],
        [4, 5, 6],
    ]  # 2x3

    matrix_b = [
        [7, 8],
        [9, 10],
        [11, 12],
    ]  # 3x2

    print(SEPARATOR)
    print("   STANDARD MATRIX MULTIPLICATION")
    print(SEPARATOR)

    print(f"\nA is {len(matrix_a)}x{len(matrix_a[0])}, B is {len(matrix_b)}x{len(matrix_b[0])}")
    print(f"Result will be {len(matrix_a)}x{len(matrix_b[0])}")

    print_matrix(matrix_a, "Matrix A")
    print_matrix(matrix_b, "Matrix B")

    matrix_c = multiply_matrices(matrix_a, matrix_b)
    print_matrix(matrix_c, "Result C = A x B (dot product)")

    print("\nOperation completed successfully.")
