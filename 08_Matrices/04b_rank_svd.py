# -------------------------------------------------
# File Name: 04b_rank_svd.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Rank from SVD: count singular values above tolerance.
# -------------------------------------------------

import numpy as np

from rank_util import A


if __name__ == "__main__":
    print("=== Rank from SVD ===\n")
    print(f"Matrix A ({A.shape[0]}x{A.shape[1]}):")
    print(A)
    _U, s, _Vt = np.linalg.svd(A, full_matrices=False)
    tol = max(A.shape) * np.finfo(s.dtype).eps
    rank_svd = int(np.sum(s > tol))
    print(f"\nSingular values: {s}")
    print(f"Tolerance (max(m,n)*eps): {tol:.2e}")
    print(f"Rank (count s > tol): {rank_svd}")
