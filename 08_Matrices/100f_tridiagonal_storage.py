# -------------------------------------------------
# File Name: 100f_tridiagonal_storage.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: Memory cost: full n×n grid vs three diagonals (3n−2).
# -------------------------------------------------

from matrix_helpers import SEPARATOR, title


def main() -> None:
    title("6. COMPARISON - Memory: full matrix vs 3 vectors")
    print(f"\n  {'n':>6}  {'Full (n^2)':>15}  {'Tridiag (3n-2)':>16}  {'Savings %':>10}")
    print("  " + "-" * 52)
    for n in [5, 10, 50, 100, 500, 1000]:
        full = n * n
        tridiag = 3 * n - 2
        savings = (1 - tridiag / full) * 100
        print(f"  {n:>6}  {full:>15,}  {tridiag:>16,}  {savings:>9.2f}%")

    print(f"\n{SEPARATOR}\n  [OK] Storage comparison done.\n{SEPARATOR}\n")


if __name__ == "__main__":
    main()
