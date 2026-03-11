# -------------------------------------------------
# File Name: 108_scalar_matrix_multiplication.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Multiply every matrix element by a scalar.
# -------------------------------------------------

"""
Scalar matrix multiplication.
Each matrix element is multiplied by the same scalar value.
"""

SEPARATOR = "=" * 40


def scalar_multiply(a: list[list[float]], scalar: float) -> list[list[float]]:
    """
    Multiply every element of a matrix by a scalar value.
    """
    if not a or not a[0]:
        raise ValueError("Matrix must be non-empty.")

    rows = len(a)
    columns = len(a[0])
    result = [[0] * columns for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            result[i][j] = a[i][j] * scalar

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
        [7, 8, 9],
    ]

    scalar_value = 3

    print(SEPARATOR)
    print("      SCALAR MULTIPLICATION")
    print(SEPARATOR)

    print_matrix(matrix_a, "Matrix A")
    print(f"\n  Scalar: {scalar_value}")

    matrix_c = scalar_multiply(matrix_a, scalar_value)

    print_matrix(matrix_c, f"Result C = {scalar_value} x A")

    print("\nOperation completed successfully.")
