# -------------------------------------------------
# File Name: 33_pca.py
# Author: Florentino Báez
# Date: 21_Machine_Learning
# Description: PCA for dimensionality reduction.
# -------------------------------------------------

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
