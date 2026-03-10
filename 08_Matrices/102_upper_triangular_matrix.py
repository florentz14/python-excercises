# -------------------------------------------------
# File Name: 102_upper_triangular_matrix.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Upper triangular matrix operations and back substitution.
# -------------------------------------------------

"""
============================================================
  UPPER TRIANGULAR MATRIX - Python 3.14
  A matrix is upper triangular when all elements BELOW
  the main diagonal are zero.

      | a  b  c  d |
      | 0  e  f  g |
      | 0  0  h  i |
      | 0  0  0  j |
============================================================
"""

import random

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


# Print matrix with aligned numeric formatting.
def print_matrix(matrix: list[list[float]], name: str = "Matrix") -> None:
    n = len(matrix)
    print(f"\n  {name} ({n}x{n}):")
    for row in matrix:
        print("    [ " + "  ".join(f"{v:6.1f}" for v in row) + " ]")


# Print vector in one line.
def print_vector(vec: list[float], name: str = "Vector") -> None:
    print(f"  {name}: [ " + "  ".join(f"{v:.1f}" for v in vec) + " ]")


# 1) Create upper triangular matrices in different ways.
def create_upper_triangular() -> list[list[float]]:
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

    return manual


# Check if a matrix is upper triangular.
def is_upper_triangular(matrix: list[list[float]]) -> bool:
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            if matrix[i][j] != 0:
                return False
    return True


# 2) Verify matrix structure.
def verify_upper_triangular(matrix: list[list[float]]) -> bool:
    title("2. VERIFY - Is it upper triangular?")

    not_triangular: list[list[float]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    for name, current in [("Our 4x4 matrix", matrix), ("Normal 3x3 matrix", not_triangular)]:
        result = is_upper_triangular(current)
        print_matrix(current, name)
        print(f"  -> Is upper triangular? {'YES' if result else 'NO'}")

    return is_upper_triangular(matrix)


# 3) Read key regions from the matrix.
def read_upper_triangular(matrix: list[list[float]]) -> None:
    title("3. READ - Access matrix regions")
    print_matrix(matrix, "Reference")

    subtitle("3a. Read main diagonal")
    diagonal = [matrix[i][i] for i in range(len(matrix))]
    print_vector(diagonal, "Main diagonal")

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


# 4) Perform common operations.
def upper_triangular_operations(a_matrix: list[list[float]]) -> None:
    title("4. OPERATIONS - Sum, transpose, scalar multiplication")
    n = len(a_matrix)

    b_matrix: list[list[float]] = [
        [2, 1, 0, 3],
        [0, 4, 5, 2],
        [0, 0, 1, 6],
        [0, 0, 0, 7],
    ]

    subtitle("4a. Sum of two upper triangular matrices")
    summed = [[a_matrix[i][j] + b_matrix[i][j] for j in range(n)] for i in range(n)]
    print_matrix(a_matrix, "Matrix A")
    print_matrix(b_matrix, "Matrix B")
    print_matrix(summed, "A + B (still upper triangular)")

    subtitle("4b. Scalar multiplication")
    k = 3.0
    scaled = [[a_matrix[i][j] * k for j in range(n)] for i in range(n)]
    print_matrix(scaled, f"A x {k:.0f}")

    subtitle("4c. Transpose (becomes lower triangular)")
    transposed = [[a_matrix[j][i] for j in range(n)] for i in range(n)]
    print_matrix(transposed, "Transpose of A -> lower triangular")


# 5) Back substitution to solve Ux = b.
def back_substitution(u_matrix: list[list[float]], b_vec: list[float]) -> list[float]:
    title("5. APPLICATION - Back substitution (solve U*x = b)")
    n = len(u_matrix)
    print_matrix(u_matrix, "Matrix U (upper triangular)")
    print_vector(b_vec, "Vector b")

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        partial_sum = sum(u_matrix[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b_vec[i] - partial_sum) / u_matrix[i][i]

    print_vector(x, "Solution x")

    # Verify that U*x is approximately b.
    print("\n  Verification U*x ~= b:")
    for i in range(n):
        calculated = sum(u_matrix[i][j] * x[j] for j in range(n))
        ok = abs(calculated - b_vec[i]) < 1e-9
        print(f"     row {i}: {calculated:.4f}  ~=  {b_vec[i]:.4f}  {'OK' if ok else 'FAIL'}")

    return x


def main() -> None:
    print(f"\n{SEPARATOR}")
    print("  UPPER TRIANGULAR MATRIX - Python 3.14")
    print(SEPARATOR)

    matrix = create_upper_triangular()
    verify_upper_triangular(matrix)
    read_upper_triangular(matrix)
    upper_triangular_operations(matrix)

    # Simple 3x3 system for back substitution.
    u3: list[list[float]] = [
        [2, 3, 1],
        [0, 4, 2],
        [0, 0, 5],
    ]
    b3: list[float] = [11, 14, 10]
    back_substitution(u3, b3)

    print(f"\n{SEPARATOR}")
    print("  [OK] Upper triangular matrix program completed.")
    print(f"{SEPARATOR}\n")


if __name__ == "__main__":
    main()
