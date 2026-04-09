# -------------------------------------------------
# File Name: 03b_max_possible_rank.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Maximum possible rank is min(num_rows, num_cols).
# -------------------------------------------------

import numpy as np

from rank_util import A


if __name__ == "__main__":
    print("=== Max possible rank: min(m, n) ===\n")
    print(f"Matrix A ({A.shape[0]}x{A.shape[1]}):")
    print(A)
    max_rank = min(A.shape)
    print(f"\nMax possible rank: min({A.shape[0]}, {A.shape[1]}) = {max_rank}")
