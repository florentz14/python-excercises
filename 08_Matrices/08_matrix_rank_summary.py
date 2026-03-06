# ------------------------------------------------------------
# File: 08_matrix_rank_summary.py
# Purpose: Summary of matrix rank analysis module.
# Description: Overview of features and key concepts.
# ------------------------------------------------------------

if __name__ == "__main__":
    print("=== Summary ===\n")
    print("Original code:")
    print("  + Works correctly")
    print("  + Uses np.linalg.matrix_rank() (recommended)")
    print("  + Simple and clear")
    print("  - No extra information")
    print("  - No matrix type analysis")
    print("  - No method comparison")
    print()
    print("Improvements:")
    print("  1. [OK] Full rank analysis")
    print("  2. [OK] Full rank vs rank deficient")
    print("  3. [OK] Method comparison (matrix_rank, SVD, QR)")
    print("  4. [OK] Different matrix type examples")
    print("  5. [OK] Rank properties")
    print("  6. [OK] Interactive mode")
    print("  7. [OK] Fundamental subspaces")
    print("  8. [OK] Documentation")
    print()
    print("Concepts:")
    print("  - Full rank: rank(A) = min(m, n)")
    print("  - Rank deficient: rank(A) < min(m, n)")
    print("  - Rank = # of linearly independent rows/columns")
    print("  - Square: full rank ⟺ determinant ≠ 0")
