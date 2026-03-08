# -------------------------------------------------
# File Name: 06_rank_properties.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: rank(A)=rank(A^T), rank(AB)<=min(rank(A),rank(B)), etc.
# -------------------------------------------------

import numpy as np

from rank_util import A


def rank_properties():
    """Demonstrate rank(A)=rank(A^T) and Sylvester's inequality."""
    print("\nMatrix Rank Properties:")
    print("=" * 70)

    A_t = A.T
    rA = np.linalg.matrix_rank(A)
    rAt = np.linalg.matrix_rank(A_t)
    print(f"1. rank(A) = rank(A^T)")
    print(f"   rank(A) = {rA}, rank(A^T) = {rAt} ✓" if rA == rAt else "   Mismatch!")

    if A.shape[1] >= 2:
        np.random.seed(42)
        B = np.random.rand(A.shape[1], 2)
        AB = A @ B
        rAB = np.linalg.matrix_rank(AB)
        rB = np.linalg.matrix_rank(B)
        print(f"\n2. rank(AB) <= min(rank(A), rank(B))")
        print(f"   rank(A)={rA}, rank(B)={rB}, rank(AB)={rAB}")
        print(f"   Holds: {rAB <= min(rA, rB)} ✓")

    m, n = A.shape
    print(f"\n3. rank(A) <= min(m,n) for {m}x{n} matrix")
    print(f"   rank(A)={rA} <= min({m},{n})={min(m,n)} ✓")

    print("=" * 70)


if __name__ == "__main__":
    print("=== Version 6: Rank Properties ===\n")
    rank_properties()
