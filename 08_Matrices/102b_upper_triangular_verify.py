# -------------------------------------------------
# File Name: 102b_upper_triangular_verify.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: Check if a matrix is upper triangular.
# -------------------------------------------------

from matrix_helpers import UPPER_4x4, print_matrix, title


def is_upper_triangular(matrix: list[list[float]]) -> bool:
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            if matrix[i][j] != 0:
                return False
    return True


def main() -> None:
    title("2. VERIFY - Is it upper triangular?")

    not_triangular: list[list[float]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    for name, current in [("Our 4x4 matrix", UPPER_4x4), ("Normal 3x3 matrix", not_triangular)]:
        result = is_upper_triangular(current)
        print_matrix(current, name)
        print(f"  -> Is upper triangular? {'YES' if result else 'NO'}")


if __name__ == "__main__":
    main()
