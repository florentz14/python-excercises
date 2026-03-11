# -------------------------------------------------
# File Name: 105_elementwise_matrix_subtraction.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Subtract two matrices element by element.
# -------------------------------------------------

"""
Element-wise matrix subtraction.
Both matrices must have the same dimensions.
"""

SEPARATOR = "=" * 40


def subtract_matrices(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """
    Subtract matrix B from matrix A element by element.
    Both matrices must have the same dimensions.
    """
    if not a or not b or not a[0] or not b[0]:
        raise ValueError("Matrices must be non-empty.")

    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Matrices must have the same dimensions.")

    rows = len(a)
    columns = len(a[0])
    result = [[0] * columns for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            result[i][j] = a[i][j] - b[i][j]

    return result


def print_matrix(matrix: list[list[float]], name: str = "Matrix") -> None:
    """Print a matrix in a readable format."""
    print(f"\n{name}:")
    for row in matrix:
        print("  ", row)


if __name__ == "__main__":
    matrix_a = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
    ]

    matrix_b = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    print(SEPARATOR)
    print("       MATRIX SUBTRACTION")
    print(SEPARATOR)

    print_matrix(matrix_a, "Matrix A")
    print_matrix(matrix_b, "Matrix B")

    matrix_c = subtract_matrices(matrix_a, matrix_b)
    print_matrix(matrix_c, "Result C = A - B")

    print("\nOperation completed successfully.")
