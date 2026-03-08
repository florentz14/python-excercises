# -------------------------------------------------
# File Name: 55_eigenvalues_eigenvectors.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: np.linalg.eig returns eigenvalues and eigenvectors.
# -------------------------------------------------

import numpy as np

A = np.array([[4, 2], [1, 3]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print("A:\n", A)
print("\nEigenvalues:", eigenvalues)
print("Eigenvectors (columns):\n", eigenvectors)

for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    Av = A @ v
    lv = eigenvalues[i] * v
    print(f"\nA @ v{i} = {Av}, lambda*v{i} = {lv} (should match)")
