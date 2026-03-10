# -------------------------------------------------
# File Name: 101_lower_triangular_matrix.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Lower triangular matrix operations and properties.
# -------------------------------------------------

"""
============================================================
  LOWER TRIANGULAR MATRIX - Python 3.14
  A matrix is lower triangular when all elements ABOVE
  the main diagonal are zero.

      | a  0  0  0 |
      | b  c  0  0 |
      | d  e  f  0 |
      | g  h  i  j |
============================================================
"""

import random

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


# Print matrix in a clean table-like format.
def print_matrix(matrix: list[list[float]], name: str = "Matrix") -> None:
    n = len(matrix)
    print(f"\n  {name} ({n}x{n}):")
    for row in matrix:
        print("    [ " + "  ".join(f"{v:6.1f}" for v in row) + " ]")


# Print vector with consistent precision.
def print_vector(vec: list[float], name: str = "Vector") -> None:
    print(f"  {name}: [ " + "  ".join(f"{v:.4f}" for v in vec) + " ]")


# 1) Create lower triangular matrices in multiple ways.
def create_lower_triangular() -> list[list[float]]:
    title("1. CREATE - Lower triangular matrix")

    subtitle("1a. Manual construction (4x4)")
    manual: list[list[float]] = [
        [6, 0, 0, 0],
        [3, 8, 0, 0],
        [7, 2, 5, 0],
        [1, 4, 9, 2],
    ]
    print_matrix(manual, "Manual")

    subtitle("1b. Loop construction (force zeros above diagonal)")
    random.seed(7)
    n = 5
    auto: list[list[float]] = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(float(random.randint(1, 9)) if j <= i else 0.0)
        auto.append(row)
    print_matrix(auto, "Auto-generated")

    subtitle("1c. From transpose of an upper triangular matrix")
    upper: list[list[float]] = [
        [4, 7, 2, 1],
        [0, 5, 3, 8],
        [0, 0, 6, 4],
        [0, 0, 0, 9],
    ]
    transposed: list[list[float]] = [[upper[j][i] for j in range(4)] for i in range(4)]
    print_matrix(upper, "Original upper triangular")
    print_matrix(transposed, "Transpose -> lower triangular")

    subtitle("1d. Construction with list comprehension")
    vals = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    comp: list[list[float]] = [
        [float(vals[i][j]) if j <= i else 0.0 for j in range(4)]
        for i in range(4)
    ]
    print_matrix(comp, "List comprehension")

    return manual


# Check if matrix is lower triangular.
def is_lower_triangular(matrix: list[list[float]]) -> bool:
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0:
                return False
    return True


# 2) Verify lower triangular structure with sample cases.
def verify_lower_triangular(matrix: list[list[float]]) -> bool:
    title("2. VERIFY - Is it lower triangular?")

    not_lower: list[list[float]] = [
        [1, 2, 3],
        [0, 5, 6],
        [0, 0, 9],
    ]

    for name, current in [("Our 4x4 matrix", matrix), ("Upper triangular 3x3 matrix", not_lower)]:
        result = is_lower_triangular(current)
        print_matrix(current, name)
        print(f"  -> Is lower triangular? {'YES' if result else 'NO'}")

    return is_lower_triangular(matrix)


# 3) Read selected areas from lower triangular matrix.
def read_lower_triangular(matrix: list[list[float]]) -> None:
    title("3. READ - Access matrix regions")
    n = len(matrix)
    print_matrix(matrix, "Reference")

    subtitle("3a. Main diagonal")
    diagonal = [matrix[i][i] for i in range(n)]
    print_vector(diagonal, "Diagonal")

    subtitle("3b. Sub-diagonal (just below main diagonal)")
    subdiagonal = [matrix[i + 1][i] for i in range(n - 1)]
    print_vector(subdiagonal, "Sub-diagonal")

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


# Basic matrix multiplication helper.
def multiply_matrices(m1: list[list[float]], m2: list[list[float]], n: int) -> list[list[float]]:
    return [[sum(m1[i][k] * m2[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


# 4) Perform operations with lower triangular matrices.
def lower_triangular_operations(a_matrix: list[list[float]]) -> None:
    title("4. OPERATIONS - Sum, scalar, multiply, transpose")
    n = len(a_matrix)

    b_matrix: list[list[float]] = [
        [3, 0, 0, 0],
        [1, 6, 0, 0],
        [5, 2, 4, 0],
        [8, 3, 1, 7],
    ]

    subtitle("4a. Sum of two lower triangular matrices")
    summed = [[a_matrix[i][j] + b_matrix[i][j] for j in range(n)] for i in range(n)]
    print_matrix(a_matrix, "Matrix A")
    print_matrix(b_matrix, "Matrix B")
    print_matrix(summed, "A + B (still lower triangular)")

    subtitle("4b. Scalar multiplication with k = 2")
    k = 2.0
    scaled = [[a_matrix[i][j] * k for j in range(n)] for i in range(n)]
    print_matrix(scaled, f"A x {k:.0f}")

    subtitle("4c. Product L*L (lower triangular remains lower)")
    product = multiply_matrices(a_matrix, b_matrix, n)
    print_matrix(product, "A x B (also lower triangular)")

    subtitle("4d. Transpose (becomes upper triangular)")
    transposed = [[a_matrix[j][i] for j in range(n)] for i in range(n)]
    print_matrix(transposed, "Transpose of A -> upper triangular")


# 5) Forward substitution to solve Lx = b.
def forward_substitution(l_matrix: list[list[float]], b_vec: list[float]) -> list[float]:
    title("5. APPLICATION - Forward substitution (solve L*x = b)")
    n = len(l_matrix)
    print_matrix(l_matrix, "Matrix L (lower triangular)")
    print_vector(b_vec, "Vector b")

    x = [0.0] * n
    for i in range(n):
        partial_sum = sum(l_matrix[i][j] * x[j] for j in range(i))
        x[i] = (b_vec[i] - partial_sum) / l_matrix[i][i]

    print_vector(x, "Solution x")

    print("\n  Verification L*x ~= b:")
    for i in range(n):
        calculated = sum(l_matrix[i][j] * x[j] for j in range(n))
        ok = abs(calculated - b_vec[i]) < 1e-9
        print(f"     row {i}: {calculated:.6f}  ~=  {b_vec[i]:.6f}  {'OK' if ok else 'FAIL'}")

    return x


# 6) Determinant equals product of diagonal entries.
def determinant_property(matrix: list[list[float]]) -> None:
    title("6. PROPERTY - Determinant equals diagonal product")
    n = len(matrix)
    det = 1.0
    print("  For triangular matrices, det(L) = product of L[i][i]\n")
    for i in range(n):
        print(f"     L[{i}][{i}] = {matrix[i][i]:.1f}")
        det *= matrix[i][i]
    print(f"\n  det(L) = {det:.1f}")


def main() -> None:
    print(f"\n{SEPARATOR}")
    print("  LOWER TRIANGULAR MATRIX - Python 3.14")
    print(SEPARATOR)

    matrix = create_lower_triangular()
    verify_lower_triangular(matrix)
    read_lower_triangular(matrix)
    lower_triangular_operations(matrix)

    l3: list[list[float]] = [
        [2, 0, 0],
        [3, 4, 0],
        [1, 5, 6],
    ]
    b3: list[float] = [4, 22, 47]
    forward_substitution(l3, b3)
    determinant_property(matrix)

    print(f"\n{SEPARATOR}")
    print("  [OK] Lower triangular matrix program completed.")
    print(f"{SEPARATOR}\n")


if __name__ == "__main__":
    main()
