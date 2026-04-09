# -------------------------------------------------
# File Name: 101e_lower_forward_substitution.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: Forward substitution to solve L x = b.
# -------------------------------------------------

from matrix_helpers import print_matrix, print_vector, title


def main() -> None:
    title("5. APPLICATION - Forward substitution (solve L*x = b)")

    l3: list[list[float]] = [
        [2, 0, 0],
        [3, 4, 0],
        [1, 5, 6],
    ]
    b3: list[float] = [4, 22, 47]
    n = len(l3)

    print_matrix(l3, "Matrix L (lower triangular)")
    print_vector(b3, "Vector b", fmt=".4f")

    x = [0.0] * n
    for i in range(n):
        partial_sum = sum(l3[i][j] * x[j] for j in range(i))
        x[i] = (b3[i] - partial_sum) / l3[i][i]

    print_vector(x, "Solution x", fmt=".4f")

    print("\n  Verification L*x ~= b:")
    for i in range(n):
        calculated = sum(l3[i][j] * x[j] for j in range(n))
        ok = abs(calculated - b3[i]) < 1e-9
        print(f"     row {i}: {calculated:.6f}  ~=  {b3[i]:.6f}  {'OK' if ok else 'FAIL'}")


if __name__ == "__main__":
    main()
