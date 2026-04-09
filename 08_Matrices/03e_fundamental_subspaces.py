# -------------------------------------------------
# File Name: 03e_fundamental_subspaces.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Dimensions of column space, row space, null space (rank-nullity).
# -------------------------------------------------

import numpy as np

from rank_util import A


if __name__ == "__main__":
    print("=== Fundamental subspaces (dimensions) ===\n")
    print(f"Matrix A ({A.shape[0]}x{A.shape[1]}):")
    print(A)
    rank = np.linalg.matrix_rank(A)
    print(f"\nRank r = {rank}")
    print(f"Column space (range) dimension: {rank}")
    print(f"Row space dimension: {rank}")

    print("\n--- Square matrix: null space (rank-nullity) ---")
    B = np.array([[1.0, 2.0, 3.0], [0.0, 1.0, 4.0], [0.0, 0.0, 1.0]])
    r = np.linalg.matrix_rank(B)
    n = B.shape[0]
    print(f"B ({n}x{n}), full rank example:")
    print(B)
    print(f"Null space dimension: n - r = {n} - {r} = {n - r}")

    S = np.array([[1.0, 2.0], [2.0, 4.0]])
    rs = np.linalg.matrix_rank(S)
    ns = S.shape[0]
    print(f"\nS ({ns}x{ns}), rank deficient:")
    print(S)
    print(f"Null space dimension: n - r = {ns} - {rs} = {ns - rs}")
