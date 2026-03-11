# -------------------------------------------------
# File Name: 107_matrix_transpose.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Transpose a matrix by swapping rows and columns.
# -------------------------------------------------

"""
Matrix transpose.
A matrix of size (m x n) becomes (n x m).
"""

SEPARATOR = "=" * 40


def transpose_matrix(a: list[list[float]]) -> list[list[float]]:
    """
    Transpose a matrix (flip rows and columns).
    A matrix of size (m x n) becomes (n x m).
    """
    if not a or not a[0]:
        raise ValueError("Matrix must be non-empty.")

    rows = len(a)
    columns = len(a[0])

    result = [[0] * rows for _ in range(columns)]
    for i in range(rows):
        for j in range(columns):
            result[j][i] = a[i][j]

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
    ]  # 2x3 matrix

    print(SEPARATOR)
    print("        MATRIX TRANSPOSE")
    print(SEPARATOR)

    print(f"\nOriginal size: {len(matrix_a)}x{len(matrix_a[0])}")
    print_matrix(matrix_a, "Matrix A")

    transposed = transpose_matrix(matrix_a)

    print(f"\nTransposed size: {len(transposed)}x{len(transposed[0])}")
    print_matrix(transposed, "Result T = A^T")

    print("\nOperation completed successfully.")
