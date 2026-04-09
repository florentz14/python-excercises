# -------------------------------------------------
# File Name: matrix_helpers.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: Print helpers and sample matrices for 100a-102e.
# -------------------------------------------------

SEPARATOR = "=" * 60

# Sample matrices (same data as original monolithic scripts)
TRIDIAG_5x5: list[list[float]] = [
    [4, 1, 0, 0, 0],
    [2, 5, 1, 0, 0],
    [0, 2, 6, 1, 0],
    [0, 0, 2, 7, 1],
    [0, 0, 0, 2, 8],
]
TRIDIAG_SUB = [2.0, 2.0, 2.0, 2.0]
TRIDIAG_DIAG = [4.0, 5.0, 6.0, 7.0, 8.0]
TRIDIAG_SUP = [1.0, 1.0, 1.0, 1.0]

LOWER_4x4: list[list[float]] = [
    [6, 0, 0, 0],
    [3, 8, 0, 0],
    [7, 2, 5, 0],
    [1, 4, 9, 2],
]

UPPER_4x4: list[list[float]] = [
    [5, 3, 7, 1],
    [0, 8, 2, 4],
    [0, 0, 6, 9],
    [0, 0, 0, 3],
]


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


def print_matrix(matrix: list[list[float]], name: str = "Matrix", fmt: str = "6.1f") -> None:
    n = len(matrix)
    print(f"\n  {name} ({n}x{n}):")
    for row in matrix:
        cells = "  ".join(format(v, fmt) for v in row)
        print(f"    [ {cells} ]")


def print_vector(
    vec: list[float],
    name: str,
    fmt: str = "5.1f",
    label_width: int | None = None,
) -> None:
    inner = "  ".join(format(v, fmt) for v in vec)
    if label_width is not None:
        print(f"  {name:{label_width}s}: [ {inner} ]")
    else:
        print(f"  {name}: [ {inner} ]")


def rebuild_matrix(sub: list[float], diag: list[float], sup: list[float]) -> list[list[float]]:
    n = len(diag)
    m = [[0.0] * n for _ in range(n)]
    for i in range(n):
        m[i][i] = diag[i]
    for i in range(n - 1):
        m[i + 1][i] = sub[i]
        m[i][i + 1] = sup[i]
    return m
