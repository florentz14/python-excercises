# -------------------------------------------------
# File Name: 100b_tridiagonal_verify.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: Test if a square matrix is tridiagonal.
# -------------------------------------------------

from matrix_helpers import TRIDIAG_5x5, print_matrix, title


def is_tridiagonal(m: list[list[float]]) -> bool:
    n = len(m)
    for i in range(n):
        for j in range(n):
            if abs(i - j) > 1 and m[i][j] != 0:
                return False
    return True


def main() -> None:
    title("2. VERIFY - Is it tridiagonal?")

    not_tridiagonal: list[list[float]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    upper_triangular: list[list[float]] = [
        [1, 2, 0],
        [0, 3, 4],
        [0, 0, 5],
    ]

    cases = [
        ("Our 5x5 matrix", TRIDIAG_5x5),
        ("Normal 3x3 matrix", not_tridiagonal),
        ("Upper triangular 3x3", upper_triangular),
    ]
    for name, current in cases:
        result = is_tridiagonal(current)
        print_matrix(current, name, fmt="5.1f")
        print(f"  -> Is tridiagonal? {'YES' if result else 'NO'}")


if __name__ == "__main__":
    main()
