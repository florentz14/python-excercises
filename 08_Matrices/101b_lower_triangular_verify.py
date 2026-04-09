# -------------------------------------------------
# File Name: 101b_lower_triangular_verify.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: Check if a matrix is lower triangular.
# -------------------------------------------------

from matrix_helpers import LOWER_4x4, print_matrix, title


def is_lower_triangular(matrix: list[list[float]]) -> bool:
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0:
                return False
    return True


def main() -> None:
    title("2. VERIFY - Is it lower triangular?")

    not_lower: list[list[float]] = [
        [1, 2, 3],
        [0, 5, 6],
        [0, 0, 9],
    ]

    for name, current in [("Our 4x4 matrix", LOWER_4x4), ("Upper triangular 3x3 matrix", not_lower)]:
        result = is_lower_triangular(current)
        print_matrix(current, name)
        print(f"  -> Is lower triangular? {'YES' if result else 'NO'}")


if __name__ == "__main__":
    main()
