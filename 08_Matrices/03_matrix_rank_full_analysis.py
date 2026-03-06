# ------------------------------------------------------------
# File: 03_matrix_rank_full_analysis.py
# Purpose: Complete analysis of matrix rank.
# Description: Rank, determinant, fundamental subspaces, full/rank-deficient.
# ------------------------------------------------------------

import numpy as np

from matrix_rank_util import A


def analyze_matrix_rank(A_mat):
    """Perform full rank analysis: rank, determinant, fundamental subspaces."""
    print("=" * 70)
    print("MATRIX RANK ANALYSIS")
    print("=" * 70)

    print(f"\nMatrix A ({A_mat.shape[0]}x{A_mat.shape[1]}):")
    print(A_mat)

    rank = np.linalg.matrix_rank(A_mat)
    print(f"\n1. Rank: {rank}")

    max_rank = min(A_mat.shape)
    print(f"2. Max possible rank: min({A_mat.shape[0]}, {A_mat.shape[1]}) = {max_rank}")

    print(f"\n3. Matrix type:")
    if rank == max_rank:
        print("   Full rank (all rows/columns linearly independent)")
    else:
        deps = max_rank - rank
        print(f"   Rank deficient ({deps} dependent row(s) or column(s))")

    # Determinant for square matrices
    if A_mat.shape[0] == A_mat.shape[1]:
        det = np.linalg.det(A_mat)
        print(f"\n4. Determinant: {det:.6f}")
        if abs(det) < 1e-10:
            print("   ~0 → singular matrix")
        else:
            print("   ≠0 → non-singular, full rank")

    print(f"\n5. Fundamental subspaces:")
    print(f"   Column space dimension: {rank}")
    print(f"   Row space dimension: {rank}")
    if A_mat.shape[0] == A_mat.shape[1]:
        print(f"   Null space dimension: {A_mat.shape[0] - rank}")

    print("=" * 70)
    return rank


if __name__ == "__main__":
    print("=== Version 3: Full Analysis ===\n")
    analyze_matrix_rank(A.copy())
