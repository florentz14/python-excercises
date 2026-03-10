# -------------------------------------------------
# File Name: 100_tridiagonal_matrix.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Tridiagonal matrix operations and Thomas algorithm.
# -------------------------------------------------

"""
============================================================
  TRIDIAGONAL MATRIX - Python 3.14
  A matrix is tridiagonal when only the main diagonal and
  the two adjacent diagonals (upper and lower) are non-zero.

      | a  b  0  0  0 |
      | c  d  e  0  0 |
      | 0  f  g  h  0 |
      | 0  0  i  j  k |
      | 0  0  0  l  m |

  It is stored efficiently with 3 vectors:
      sub-diagonal   (c, f, i, l)
      main diagonal  (a, d, g, j, m)
      super-diagonal (b, e, h, k)
============================================================
"""

import random

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


# Printing helper for square matrices.
def print_matrix(matrix: list[list[float]], name: str = "Matrix") -> None:
    n = len(matrix)
    print(f"\n  {name} ({n}x{n}):")
    for row in matrix:
        print("    [ " + "  ".join(f"{v:5.1f}" for v in row) + " ]")


# Printing helper for vectors.
def print_vector(vec: list[float], name: str) -> None:
    print(f"  {name:20s}: [ " + "  ".join(f"{v:5.1f}" for v in vec) + " ]")


# Build a full matrix from tridiagonal vectors.
def rebuild_matrix(sub: list[float], diag: list[float], sup: list[float]) -> list[list[float]]:
    n = len(diag)
    m = [[0.0] * n for _ in range(n)]
    for i in range(n):
        m[i][i] = diag[i]
    for i in range(n - 1):
        m[i + 1][i] = sub[i]
        m[i][i + 1] = sup[i]
    return m


# 1) Create tridiagonal matrix representations.
def create_tridiagonal() -> tuple[list[list[float]], list[float], list[float], list[float]]:
    title("1. CREATE - Tridiagonal matrix (two representations)")

    subtitle("1a. Full 5x5 matrix (explicit zeros)")
    matrix: list[list[float]] = [
        [4, 1, 0, 0, 0],
        [2, 5, 1, 0, 0],
        [0, 2, 6, 1, 0],
        [0, 0, 2, 7, 1],
        [0, 0, 0, 2, 8],
    ]
    print_matrix(matrix, "Full tridiagonal")

    subtitle("1b. Compact representation with 3 vectors")
    sub = [2.0, 2.0, 2.0, 2.0]
    diag = [4.0, 5.0, 6.0, 7.0, 8.0]
    sup = [1.0, 1.0, 1.0, 1.0]
    print_vector(sub, "Sub-diagonal  (a)")
    print_vector(diag, "Main diagonal (d)")
    print_vector(sup, "Super-diag    (b)")

    subtitle("1c. Rebuild full matrix from vectors")
    rebuilt = rebuild_matrix(sub, diag, sup)
    print_matrix(rebuilt, "Rebuilt from vectors")

    subtitle("1d. Auto-generate random tridiagonal matrix")
    random.seed(99)
    n2 = 6
    d2 = [float(random.randint(5, 10)) for _ in range(n2)]
    s2 = [float(random.randint(1, 3)) for _ in range(n2 - 1)]
    u2 = [float(random.randint(1, 3)) for _ in range(n2 - 1)]
    print_vector(s2, "Sub-diagonal  (a)")
    print_vector(d2, "Main diagonal (d)")
    print_vector(u2, "Super-diag    (b)")
    print_matrix(rebuild_matrix(s2, d2, u2), f"Random tridiagonal {n2}x{n2}")

    return matrix, sub, diag, sup


# Check whether a matrix is tridiagonal.
def is_tridiagonal(m: list[list[float]]) -> bool:
    n = len(m)
    for i in range(n):
        for j in range(n):
            if abs(i - j) > 1 and m[i][j] != 0:
                return False
    return True


# 2) Verify tridiagonal structure with examples.
def verify_tridiagonal(matrix: list[list[float]]) -> bool:
    title("2. VERIFY - Is it tridiagonal?")

    not_tridiagonal: list[list[float]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    upper_triangular: list[list[float]] = [
        [1, 2, 0],
        [0, 3, 4],
        [0, 0, 5],
    ]

    cases = [
        ("Our 5x5 matrix", matrix),
        ("Normal 3x3 matrix", not_tridiagonal),
        ("Upper triangular 3x3", upper_triangular),
    ]
    for name, current in cases:
        result = is_tridiagonal(current)
        print_matrix(current, name)
        print(f"  -> Is tridiagonal? {'YES' if result else 'NO'}")

    return is_tridiagonal(matrix)


# 3) Read tridiagonal diagonals and basic metrics.
def read_tridiagonal(matrix: list[list[float]]) -> None:
    title("3. READ - Three diagonals and statistics")
    n = len(matrix)
    print_matrix(matrix, "Reference")

    subtitle("3a. Extract the three diagonals")
    main_diag = [matrix[i][i] for i in range(n)]
    super_diag = [matrix[i][i + 1] for i in range(n - 1)]
    sub_diag = [matrix[i + 1][i] for i in range(n - 1)]
    print_vector(sub_diag, "Sub-diagonal")
    print_vector(main_diag, "Main diagonal")
    print_vector(super_diag, "Super-diagonal")

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


# 4) Perform operations on tridiagonal matrices.
def tridiagonal_operations(a_matrix: list[list[float]]) -> None:
    title("4. OPERATIONS - Sum, scalar, matrix-vector product")
    n = len(a_matrix)

    b_matrix: list[list[float]] = [
        [1, 2, 0, 0, 0],
        [3, 1, 2, 0, 0],
        [0, 3, 1, 2, 0],
        [0, 0, 3, 1, 2],
        [0, 0, 0, 3, 1],
    ]

    subtitle("4a. Sum of two tridiagonal matrices")
    summed = [[a_matrix[i][j] + b_matrix[i][j] for j in range(n)] for i in range(n)]
    print_matrix(a_matrix, "Matrix A")
    print_matrix(b_matrix, "Matrix B")
    print_matrix(summed, "A + B (still tridiagonal)")

    subtitle("4b. Scalar multiplication with k = 2")
    k = 2.0
    scaled = [[a_matrix[i][j] * k for j in range(n)] for i in range(n)]
    print_matrix(scaled, f"A x {k:.0f}")

    subtitle("4c. Efficient matrix-vector product (use 3 diagonals)")
    x_vec = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(f"  Vector x: {x_vec}")

    # Standard O(n^2) matrix-vector multiplication.
    y_standard = [sum(a_matrix[i][j] * x_vec[j] for j in range(n)) for i in range(n)]

    # Efficient O(n) multiplication with tridiagonal vectors.
    diag = [a_matrix[i][i] for i in range(n)]
    sup = [a_matrix[i][i + 1] for i in range(n - 1)]
    sub = [a_matrix[i + 1][i] for i in range(n - 1)]

    y_fast = [0.0] * n
    y_fast[0] = diag[0] * x_vec[0] + sup[0] * x_vec[1]
    for i in range(1, n - 1):
        y_fast[i] = sub[i - 1] * x_vec[i - 1] + diag[i] * x_vec[i] + sup[i] * x_vec[i + 1]
    y_fast[n - 1] = sub[n - 2] * x_vec[n - 2] + diag[n - 1] * x_vec[n - 1]

    print_vector(y_standard, "A*x (standard O(n^2))")
    print_vector(y_fast, "A*x (efficient O(n))")
    same = all(abs(left - right) < 1e-9 for left, right in zip(y_standard, y_fast))
    print(f"  Same results? {'YES' if same else 'NO'}")


# 5) Thomas algorithm for Ax = b, tridiagonal only.
def thomas_algorithm(
    sub: list[float],   # sub-diagonal (n-1)
    diag: list[float],  # main diagonal (n)
    sup: list[float],   # super-diagonal (n-1)
    rhs: list[float],   # right-hand side (n)
) -> list[float]:
    title("5. THOMAS ALGORITHM - Solve tridiagonal system in O(n)")
    n = len(diag)

    print("  Tridiagonal system:")
    print("  sub-diag a:", sub)
    print("  diag     d:", diag)
    print("  sup-diag c:", sup)
    print("  rhs      b:", rhs)

    # Work on copies to avoid changing input vectors.
    d2 = diag[:]
    b2 = rhs[:]

    subtitle("5a. Forward sweep")
    for i in range(1, n):
        factor = sub[i - 1] / d2[i - 1]
        d2[i] = d2[i] - factor * sup[i - 1]
        b2[i] = b2[i] - factor * b2[i - 1]
        print(f"     i={i}: factor={factor:.4f}  d[{i}]={d2[i]:.4f}  b[{i}]={b2[i]:.4f}")

    subtitle("5b. Back substitution")
    x = [0.0] * n
    x[n - 1] = b2[n - 1] / d2[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = (b2[i] - sup[i] * x[i + 1]) / d2[i]
    print_vector(x, "Solution x")

    subtitle("5c. Verification")
    for i in range(n):
        calculated = diag[i] * x[i]
        if i > 0:
            calculated += sub[i - 1] * x[i - 1]
        if i < n - 1:
            calculated += sup[i] * x[i + 1]
        ok = abs(calculated - rhs[i]) < 1e-9
        print(f"     row {i}: calculated={calculated:.6f}  expected={rhs[i]:.6f}  {'OK' if ok else 'FAIL'}")

    return x


# 6) Compare storage cost full vs compact form.
def compare_storage() -> None:
    title("6. COMPARISON - Memory: full matrix vs 3 vectors")
    print(f"\n  {'n':>6}  {'Full (n^2)':>15}  {'Tridiag (3n-2)':>16}  {'Savings %':>10}")
    print("  " + "-" * 52)
    for n in [5, 10, 50, 100, 500, 1000]:
        full = n * n
        tridiag = 3 * n - 2
        savings = (1 - tridiag / full) * 100
        print(f"  {n:>6}  {full:>15,}  {tridiag:>16,}  {savings:>9.2f}%")


def main() -> None:
    print(f"\n{SEPARATOR}")
    print("  TRIDIAGONAL MATRIX - Python 3.14")
    print(SEPARATOR)

    matrix, _, _, _ = create_tridiagonal()
    verify_tridiagonal(matrix)
    read_tridiagonal(matrix)
    tridiagonal_operations(matrix)

    # 5x5 tridiagonal system for Thomas algorithm.
    sub_t = [2.0, 2.0, 2.0, 2.0]
    diag_t = [4.0, 5.0, 6.0, 7.0, 8.0]
    sup_t = [1.0, 1.0, 1.0, 1.0]
    rhs_t = [6.0, 13.0, 16.0, 22.0, 26.0]
    thomas_algorithm(sub_t, diag_t, sup_t, rhs_t)

    compare_storage()

    print(f"\n{SEPARATOR}")
    print("  [OK] Tridiagonal matrix program completed.")
    print(f"{SEPARATOR}\n")


if __name__ == "__main__":
    main()
