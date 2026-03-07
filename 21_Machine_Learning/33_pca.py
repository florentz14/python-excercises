"""
Principal Component Analysis (PCA) - Dimensionality Reduction
=============================================================
Reduces many columns while preserving as much information as possible.
Useful before visualization or to speed up models.

Author: Florentino Báez
"""

from sklearn.decomposition import PCA

# Example dataset (3 dimensions)
X = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [8, 8, 9],
    [9, 9, 10]
]

# Create PCA and transform
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print("Reduced data:")
print(X_reduced)
