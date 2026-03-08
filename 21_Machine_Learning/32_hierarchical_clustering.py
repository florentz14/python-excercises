# -------------------------------------------------
# File Name: 32_hierarchical_clustering.py
# Author: Florentino Báez
# Date: 21_Machine_Learning
# Description: Hierarchical clustering for hierarchical grouping.
# -------------------------------------------------

from sklearn.cluster import AgglomerativeClustering

# Example dataset
X = [[1, 2], [1, 3], [2, 2], [8, 8], [9, 8], [8, 9]]

# Create model
model = AgglomerativeClustering(n_clusters=2)

# Get clusters
labels = model.fit_predict(X)

print("Cluster labels:", labels)
