# -------------------------------------------------
# File Name: 04a_rank_matrix_rank.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Rank via np.linalg.matrix_rank (default algorithm in NumPy).
# -------------------------------------------------

import numpy as np

from rank_util import A


if __name__ == "__main__":
    print("=== Rank: np.linalg.matrix_rank ===\n")
    print(f"Matrix A ({A.shape[0]}x{A.shape[1]}):")
    print(A)
    rank = np.linalg.matrix_rank(A)
    print(f"\nmatrix_rank(A) = {rank}")
