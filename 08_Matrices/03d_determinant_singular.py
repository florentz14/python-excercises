# -------------------------------------------------
# File Name: 03d_determinant_singular.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Determinant for square matrices; singular vs non-singular.
# -------------------------------------------------

import numpy as np


if __name__ == "__main__":
    print("=== Determinant (square matrices only) ===\n")
    B = np.array([[2.0, 1.0], [1.0, 3.0]])
    print("Non-singular example B (2x2):")
    print(B)
    det_b = np.linalg.det(B)
    print(f"det(B) = {det_b:.6f}  ->  non-singular, full rank\n")

    S = np.array([[1.0, 2.0], [2.0, 4.0]])
    print("Singular example S (2x2), second row is multiple of first:")
    print(S)
    det_s = np.linalg.det(S)
    print(f"det(S) = {det_s:.6f}")
    if abs(det_s) < 1e-10:
        print("~0  ->  singular matrix (not invertible).")
