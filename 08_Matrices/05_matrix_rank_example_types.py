# ------------------------------------------------------------
# File: 05_matrix_rank_example_types.py
# Purpose: Rank examples for different matrix types.
# Description: Identity, full rank, rank deficient, zero, rectangular.
# ------------------------------------------------------------

import numpy as np

from matrix_rank_util import A


def rank_examples():
    """Show rank for various matrix types."""
    print("\nRank examples for different matrices:")
    print("=" * 70)

    examples = {
        "Identity 3x3": np.eye(3),
        "Full rank 2x2": np.array([[1, 2], [3, 4]]),
        "Rank deficient": np.array([[1, 2], [2, 4]]),
        "Original example": A,
        "Zero matrix": np.zeros((3, 3)),
        "Rectangular (more cols)": np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]),
        "Rectangular (more rows)": np.array([[1, 2], [3, 4], [5, 6], [7, 8]]),
    }

    for name, mat in examples.items():
        rank = np.linalg.matrix_rank(mat)
        max_r = min(mat.shape)
        t = "Full" if rank == max_r else "Deficient"
        print(f"\n{name}: shape={mat.shape}, rank={rank}/{max_r} ({t})")
        if mat.size <= 16:
            print(f"  Matrix:\n{mat}")

    print("=" * 70)


if __name__ == "__main__":
    print("=== Version 5: Example Types ===\n")
    rank_examples()
