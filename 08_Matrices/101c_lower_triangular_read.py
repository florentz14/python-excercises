# -------------------------------------------------
# File Name: 101c_lower_triangular_read.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: Read diagonal, sub-diagonal, and lower-zone statistics.
# -------------------------------------------------

from matrix_helpers import LOWER_4x4, print_matrix, print_vector, subtitle, title


def main() -> None:
    matrix = LOWER_4x4
    title("3. READ - Access matrix regions")
    n = len(matrix)
    print_matrix(matrix, "Reference")

    subtitle("3a. Main diagonal")
    diagonal = [matrix[i][i] for i in range(n)]
    print_vector(diagonal, "Diagonal", fmt=".4f")

    subtitle("3b. Sub-diagonal (just below main diagonal)")
    subdiagonal = [matrix[i + 1][i] for i in range(n - 1)]
    print_vector(subdiagonal, "Sub-diagonal", fmt=".4f")

    subtitle("3c. Non-zero zone elements with positions")
    print("  Elements (row, col, value):")
    for i in range(n):
        for j in range(i + 1):
            print(f"     M[{i}][{j}] = {matrix[i][j]:.0f}")

    subtitle("3d. Statistics of lower zone")
    values = [matrix[i][j] for i in range(n) for j in range(i + 1)]
    print(f"  Total non-zero elements : {len(values)}")
    print(f"  Sum                     : {sum(values):.1f}")
    print(f"  Average                 : {sum(values)/len(values):.2f}")
    print(f"  Maximum                 : {max(values):.1f}")
    print(f"  Minimum                 : {min(values):.1f}")
    trace = sum(matrix[i][i] for i in range(n))
    print(f"  Trace (sum diagonal)    : {trace:.1f}")


if __name__ == "__main__":
    main()
