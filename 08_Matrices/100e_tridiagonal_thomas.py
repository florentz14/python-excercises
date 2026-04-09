# -------------------------------------------------
# File Name: 100e_tridiagonal_thomas.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: Thomas algorithm to solve a tridiagonal Ax = b in O(n).
# -------------------------------------------------

from matrix_helpers import TRIDIAG_SUB, TRIDIAG_DIAG, TRIDIAG_SUP, print_vector, subtitle, title


def thomas_algorithm(
    sub: list[float],
    diag: list[float],
    sup: list[float],
    rhs: list[float],
) -> list[float]:
    title("5. THOMAS ALGORITHM - Solve tridiagonal system in O(n)")
    n = len(diag)

    print("  Tridiagonal system:")
    print("  sub-diag a:", sub)
    print("  diag     d:", diag)
    print("  sup-diag c:", sup)
    print("  rhs      b:", rhs)

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


def main() -> None:
    sub_t = list(TRIDIAG_SUB)
    diag_t = list(TRIDIAG_DIAG)
    sup_t = list(TRIDIAG_SUP)
    rhs_t = [6.0, 13.0, 16.0, 22.0, 26.0]
    thomas_algorithm(sub_t, diag_t, sup_t, rhs_t)


if __name__ == "__main__":
    main()
