# -------------------------------------------------
# File Name: 101f_lower_determinant_diagonal.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: For triangular L, det(L) = product of diagonal entries.
# -------------------------------------------------

from matrix_helpers import LOWER_4x4, title


def main() -> None:
    matrix = LOWER_4x4
    title("6. PROPERTY - Determinant equals diagonal product")
    n = len(matrix)
    det = 1.0
    print("  For triangular matrices, det(L) = product of L[i][i]\n")
    for i in range(n):
        print(f"     L[{i}][{i}] = {matrix[i][i]:.1f}")
        det *= matrix[i][i]
    print(f"\n  det(L) = {det:.1f}")


if __name__ == "__main__":
    main()
