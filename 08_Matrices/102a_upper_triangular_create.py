# -------------------------------------------------
# File Name: 102a_upper_triangular_create.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: Build upper triangular matrices (manual, loops, comprehension).
# -------------------------------------------------

import random

from matrix_helpers import print_matrix, subtitle, title


def main() -> None:
    title("1. CREATE - Upper triangular matrix")

    subtitle("1a. Manual construction (4x4)")
    manual: list[list[float]] = [
        [5, 3, 7, 1],
        [0, 8, 2, 4],
        [0, 0, 6, 9],
        [0, 0, 0, 3],
    ]
    print_matrix(manual, "Manual")

    subtitle("1b. Loop construction (force zeros below diagonal)")
    random.seed(42)
    n = 5
    auto: list[list[float]] = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(float(random.randint(1, 9)) if j >= i else 0.0)
        auto.append(row)
    print_matrix(auto, "Auto-generated")

    subtitle("1c. Construction with list comprehension")
    vals = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    comp: list[list[float]] = [
        [float(vals[i][j]) if j >= i else 0.0 for j in range(4)]
        for i in range(4)
    ]
    print_matrix(comp, "List comprehension")


if __name__ == "__main__":
    main()
