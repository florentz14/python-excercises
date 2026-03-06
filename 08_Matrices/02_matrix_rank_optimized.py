# ------------------------------------------------------------
# File: 02_matrix_rank_optimized.py
# Purpose: Matrix rank with enhanced information output.
# Description: Uses shared utility for rank computation and detailed info.
# ------------------------------------------------------------

from matrix_rank_util import A, compute_matrix_rank


if __name__ == "__main__":
    print("=== Version 2: Optimized ===\n")
    rank, info = compute_matrix_rank(A.copy())
