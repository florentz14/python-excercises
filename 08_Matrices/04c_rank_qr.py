# -------------------------------------------------
# File Name: 04c_rank_qr.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Rank from QR: non-zero diagonal entries of R (heuristic).
# -------------------------------------------------

import numpy as np

from rank_util import A


if __name__ == "__main__":
    print("=== Rank from QR (R diagonal) ===\n")
    print(f"Matrix A ({A.shape[0]}x{A.shape[1]}):")
    print(A)
    try:
        _Q, R = np.linalg.qr(A)
        diag = np.abs(np.diag(R))
        rank_qr = int(np.sum(diag > 1e-10))
        print(f"\n|diag(R)|: {diag}")
        print(f"Rank (count |R_ii| > 1e-10): {rank_qr}")
    except Exception as e:
        print(f"\nQR failed: {e}")
