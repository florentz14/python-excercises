# -------------------------------------------------
# File Name: 102c_upper_triangular_read.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: Read diagonal, upper region, sums, trace.
# -------------------------------------------------

from matrix_helpers import UPPER_4x4, print_matrix, print_vector, subtitle, title


def main() -> None:
    matrix = UPPER_4x4
    title("3. READ - Access matrix regions")
    print_matrix(matrix, "Reference")

    subtitle("3a. Read main diagonal")
    diagonal = [matrix[i][i] for i in range(len(matrix))]
    print_vector(diagonal, "Main diagonal", fmt=".1f")

    subtitle("3b. Read non-zero elements (upper region)")
    print("  Elements (row, col, value):")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j >= i:
                print(f"     M[{i}][{j}] = {matrix[i][j]:.0f}")

    subtitle("3c. Sum of upper triangular region")
    total = sum(matrix[i][j] for i in range(len(matrix)) for j in range(i, len(matrix)))
    print(f"  Total sum in upper region: {total:.1f}")

    subtitle("3d. Trace (sum of main diagonal)")
    trace = sum(matrix[i][i] for i in range(len(matrix)))
    print(f"  Trace = {trace:.1f}")


if __name__ == "__main__":
    main()
