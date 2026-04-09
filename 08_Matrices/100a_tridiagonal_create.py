# -------------------------------------------------
# File Name: 100a_tridiagonal_create.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: Build tridiagonal matrices (full grid vs three diagonals).
# -------------------------------------------------

import random

from matrix_helpers import (
    TRIDIAG_DIAG,
    TRIDIAG_SUB,
    TRIDIAG_SUP,
    print_matrix,
    print_vector,
    rebuild_matrix,
    subtitle,
    title,
)


def main() -> None:
    title("1. CREATE - Tridiagonal matrix (two representations)")

    subtitle("1a. Full 5x5 matrix (explicit zeros)")
    matrix: list[list[float]] = [
        [4, 1, 0, 0, 0],
        [2, 5, 1, 0, 0],
        [0, 2, 6, 1, 0],
        [0, 0, 2, 7, 1],
        [0, 0, 0, 2, 8],
    ]
    print_matrix(matrix, "Full tridiagonal", fmt="5.1f")

    subtitle("1b. Compact representation with 3 vectors")
    sub, diag, sup = list(TRIDIAG_SUB), list(TRIDIAG_DIAG), list(TRIDIAG_SUP)
    print_vector(sub, "Sub-diagonal  (a)", label_width=20)
    print_vector(diag, "Main diagonal (d)", label_width=20)
    print_vector(sup, "Super-diag    (b)", label_width=20)

    subtitle("1c. Rebuild full matrix from vectors")
    print_matrix(rebuild_matrix(sub, diag, sup), "Rebuilt from vectors", fmt="5.1f")

    subtitle("1d. Auto-generate random tridiagonal matrix")
    random.seed(99)
    n2 = 6
    d2 = [float(random.randint(5, 10)) for _ in range(n2)]
    s2 = [float(random.randint(1, 3)) for _ in range(n2 - 1)]
    u2 = [float(random.randint(1, 3)) for _ in range(n2 - 1)]
    print_vector(s2, "Sub-diagonal  (a)", label_width=20)
    print_vector(d2, "Main diagonal (d)", label_width=20)
    print_vector(u2, "Super-diag    (b)", label_width=20)
    print_matrix(rebuild_matrix(s2, d2, u2), f"Random tridiagonal {n2}x{n2}", fmt="5.1f")


if __name__ == "__main__":
    main()
