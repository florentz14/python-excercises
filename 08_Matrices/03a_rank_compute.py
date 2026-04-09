# -------------------------------------------------
# File Name: 03a_rank_compute.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Rank of a matrix with np.linalg.matrix_rank.
# -------------------------------------------------

import numpy as np

from rank_util import A


if __name__ == "__main__":
    print("=== Rank: number of independent rows/columns ===\n")
    print(f"Matrix A ({A.shape[0]}x{A.shape[1]}):")
    print(A)
    rank = np.linalg.matrix_rank(A)
    print(f"\nRank: {rank}")
