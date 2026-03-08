# -------------------------------------------------
# File Name: 02_rank_optimized.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Uses shared utility for rank computation and detailed info.
# -------------------------------------------------

from rank_util import A, compute_matrix_rank


if __name__ == "__main__":
    print("=== Version 2: Optimized ===\n")
    rank, info = compute_matrix_rank(A.copy())
