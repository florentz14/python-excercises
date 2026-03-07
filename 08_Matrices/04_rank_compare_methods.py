# ------------------------------------------------------------
# File: 04_rank_compare_methods.py
# Purpose: Compare methods for computing matrix rank.
# Description: matrix_rank(), SVD, and QR decomposition.
# ------------------------------------------------------------

import numpy as np

from rank_util import A


def compare_rank_methods(A_mat):
    """Compare matrix_rank, SVD, and QR for rank computation."""
    print("\nComparing rank methods:")
    print("=" * 60)

    rank1 = np.linalg.matrix_rank(A_mat)
    print(f"1. np.linalg.matrix_rank(): {rank1}")

    # SVD: rank = number of singular values above tolerance
    U, s, Vt = np.linalg.svd(A_mat, full_matrices=False)
    tol = max(A_mat.shape) * np.finfo(s.dtype).eps
    rank2 = int(np.sum(s > tol))
    print(f"2. SVD (singular values > tol): {rank2}")
    print(f"   Singular values: {s}")

    # QR: rank = non-zero diagonal entries of R
    try:
        Q, R = np.linalg.qr(A_mat)
        rank3 = int(np.sum(np.abs(np.diag(R)) > 1e-10))
        print(f"3. QR (non-zero diagonals): {rank3}")
    except Exception as e:
        print(f"3. QR: Error - {e}")
        rank3 = rank1

    print("=" * 60)
    print(f"All methods consistent: {rank1 == rank2 == rank3}")
    return rank1


if __name__ == "__main__":
    print("=== Version 4: Method Comparison ===\n")
    compare_rank_methods(A.copy())
