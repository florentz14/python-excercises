# -------------------------------------------------
# File Name: 01_rank_original.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Basic example that computes rank of a matrix.
# -------------------------------------------------

import numpy as np


def matrix_rank_original():
    """Compute and print matrix rank (original version)."""
    a = np.array([[1, 2, 3, 4], [0, 2, -1, 5], [0, 0, 3, 7]])
    print(a)
    result = np.linalg.matrix_rank(a)
    print(result)


if __name__ == "__main__":
    print("=== Matrix Rank ===\n")
    print("Rank = number of linearly independent rows (or columns).\n")
    print("=== Version 1: Original ===\n")
    matrix_rank_original()
