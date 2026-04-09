# -------------------------------------------------
# File Name: 100c_tridiagonal_read.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: Read the three diagonals, stats, and selected entries.
# -------------------------------------------------

from matrix_helpers import TRIDIAG_5x5, print_matrix, print_vector, subtitle, title


def main() -> None:
    matrix = TRIDIAG_5x5
    title("3. READ - Three diagonals and statistics")
    n = len(matrix)
    print_matrix(matrix, "Reference", fmt="5.1f")

    subtitle("3a. Extract the three diagonals")
    main_diag = [matrix[i][i] for i in range(n)]
    super_diag = [matrix[i][i + 1] for i in range(n - 1)]
    sub_diag = [matrix[i + 1][i] for i in range(n - 1)]
    print_vector(sub_diag, "Sub-diagonal", label_width=20)
    print_vector(main_diag, "Main diagonal", label_width=20)
    print_vector(super_diag, "Super-diagonal", label_width=20)

    subtitle("3b. Count non-zero vs total elements")
    total = n * n
    non_zero = n + 2 * (n - 1)
    zero_count = total - non_zero
    print(f"  Size n x n            : {total} elements")
    print(f"  Non-zero elements     : {non_zero}  ({non_zero / total * 100:.1f}%)")
    print(f"  Zero elements         : {zero_count}  ({zero_count / total * 100:.1f}%)")
    print(f"  -> Memory savings     : {zero_count / total * 100:.1f}% using 3 vectors")

    subtitle("3c. Access any element M[i][j]")
    for row, col in [(0, 0), (1, 0), (2, 3), (3, 1), (4, 4)]:
        print(f"     M[{row}][{col}] = {matrix[row][col]:.1f}")

    subtitle("3d. Trace and diagonal sums")
    print(f"  Trace (sum main diag) : {sum(main_diag):.1f}")
    print(f"  Sub-diagonal sum      : {sum(sub_diag):.1f}")
    print(f"  Super-diagonal sum    : {sum(super_diag):.1f}")


if __name__ == "__main__":
    main()
