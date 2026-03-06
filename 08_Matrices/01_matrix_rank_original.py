# ------------------------------------------------------------
# File: 01_matrix_rank_original.py
# Purpose: Original matrix rank computation using NumPy.
# Description: Basic example that computes rank of a matrix.
# ------------------------------------------------------------

import numpy as np


def matrix_rank_original():
    """Compute and print matrix rank (original version)."""
    A = np.array([[1, 2, 3, 4], [0, 2, -1, 5], [0, 0, 3, 7]])
    print(A)
    result = np.linalg.matrix_rank(A)
    print(result)


if __name__ == "__main__":
    print("=== Matrix Rank ===\n")
    print("Rank = number of linearly independent rows (or columns).\n")
    print("=== Version 1: Original ===\n")
    matrix_rank_original()
