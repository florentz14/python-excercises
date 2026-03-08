# -------------------------------------------------
# File Name: rank_util.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Sample matrix A and compute_matrix_rank() with optional details.
# -------------------------------------------------

import numpy as np

# Sample matrix for examples (3x4)
A = np.array([[1, 2, 3, 4], [0, 2, -1, 5], [0, 0, 3, 7]])


def compute_matrix_rank(A_mat, show_info=True):
    """
    Compute matrix rank and optional detailed analysis.
    Returns: (rank, info_dict)
    """
    rank = np.linalg.matrix_rank(A_mat)

    if show_info:
        print(f"Matrix ({A_mat.shape[0]}x{A_mat.shape[1]}):")
        print(A_mat)
        print(f"\nRank: {rank}")
        print(f"Max rank possible: min({A_mat.shape[0]}, {A_mat.shape[1]}) = {min(A_mat.shape)}")
        if rank == min(A_mat.shape):
            print("Full rank matrix")
        else:
            print("Rank deficient matrix")
            print(f"   Dependencies: {min(A_mat.shape) - rank} row(s) or column(s)")

    info = {
        "rank": rank,
        "shape": A_mat.shape,
        "max_rank": min(A_mat.shape),
        "full_rank": rank == min(A_mat.shape),
    }
    return rank, info


# Alias for backward compatibility
calcular_rango_matriz = compute_matrix_rank
