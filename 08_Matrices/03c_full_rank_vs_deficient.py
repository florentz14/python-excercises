# -------------------------------------------------
# File Name: 03c_full_rank_vs_deficient.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Full rank vs rank-deficient matrices.
# -------------------------------------------------

import numpy as np

from rank_util import A


if __name__ == "__main__":
    print("=== Full rank vs rank deficient ===\n")
    print(f"Matrix A ({A.shape[0]}x{A.shape[1]}):")
    print(A)
    rank = np.linalg.matrix_rank(A)
    max_rank = min(A.shape)
    print(f"\nRank: {rank}  |  max possible: {max_rank}")
    if rank == max_rank:
        print("Type: full rank (rows and columns are as independent as possible).")
    else:
        deps = max_rank - rank
        print(f"Type: rank deficient ({deps} dependent row(s) or column(s)).")
