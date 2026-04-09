# -------------------------------------------------
# File Name: 102e_upper_back_substitution.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: Back substitution to solve U x = b.
# -------------------------------------------------

from matrix_helpers import print_matrix, print_vector, title


def main() -> None:
    title("5. APPLICATION - Back substitution (solve U*x = b)")

    u3: list[list[float]] = [
        [2, 3, 1],
        [0, 4, 2],
        [0, 0, 5],
    ]
    b3: list[float] = [11, 14, 10]
    n = len(u3)

    print_matrix(u3, "Matrix U (upper triangular)")
    print_vector(b3, "Vector b", fmt=".1f")

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        partial_sum = sum(u3[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b3[i] - partial_sum) / u3[i][i]

    print_vector(x, "Solution x", fmt=".1f")

    print("\n  Verification U*x ~= b:")
    for i in range(n):
        calculated = sum(u3[i][j] * x[j] for j in range(n))
        ok = abs(calculated - b3[i]) < 1e-9
        print(f"     row {i}: {calculated:.4f}  ~=  {b3[i]:.4f}  {'OK' if ok else 'FAIL'}")


if __name__ == "__main__":
    main()
