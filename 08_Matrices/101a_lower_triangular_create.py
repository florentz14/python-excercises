# -------------------------------------------------
# File Name: 101a_lower_triangular_create.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: Build lower triangular matrices (manual, loops, transpose).
# -------------------------------------------------

import random

from matrix_helpers import print_matrix, subtitle, title


def main() -> None:
    title("1. CREATE - Lower triangular matrix")

    subtitle("1a. Manual construction (4x4)")
    manual: list[list[float]] = [
        [6, 0, 0, 0],
        [3, 8, 0, 0],
        [7, 2, 5, 0],
        [1, 4, 9, 2],
    ]
    print_matrix(manual, "Manual")

    subtitle("1b. Loop construction (force zeros above diagonal)")
    random.seed(7)
    n = 5
    auto: list[list[float]] = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(float(random.randint(1, 9)) if j <= i else 0.0)
        auto.append(row)
    print_matrix(auto, "Auto-generated")

    subtitle("1c. From transpose of an upper triangular matrix")
    upper: list[list[float]] = [
        [4, 7, 2, 1],
        [0, 5, 3, 8],
        [0, 0, 6, 4],
        [0, 0, 0, 9],
    ]
    transposed: list[list[float]] = [[upper[j][i] for j in range(4)] for i in range(4)]
    print_matrix(upper, "Original upper triangular")
    print_matrix(transposed, "Transpose -> lower triangular")

    subtitle("1d. Construction with list comprehension")
    vals = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    comp: list[list[float]] = [
        [float(vals[i][j]) if j <= i else 0.0 for j in range(4)]
        for i in range(4)
    ]
    print_matrix(comp, "List comprehension")


if __name__ == "__main__":
    main()
