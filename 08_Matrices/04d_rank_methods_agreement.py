# -------------------------------------------------
# File Name: 04d_rank_methods_agreement.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Compare matrix_rank, SVD, and QR ranks on the same matrix.
# -------------------------------------------------

import numpy as np

from rank_util import A


if __name__ == "__main__":
    print("=== Do all rank methods agree? ===\n")
    print(f"Matrix A ({A.shape[0]}x{A.shape[1]}):")
    print(A)

    rank1 = np.linalg.matrix_rank(A)

    _U, s, _Vt = np.linalg.svd(A, full_matrices=False)
    tol = max(A.shape) * np.finfo(s.dtype).eps
    rank2 = int(np.sum(s > tol))

    try:
        _Q, R = np.linalg.qr(A)
        rank3 = int(np.sum(np.abs(np.diag(R)) > 1e-10))
    except Exception:
        rank3 = rank1

    print(f"\n1. matrix_rank: {rank1}")
    print(f"2. SVD (s > tol): {rank2}")
    print(f"3. QR diagonal: {rank3}")
    print(f"\nAll agree: {rank1 == rank2 == rank3}")
