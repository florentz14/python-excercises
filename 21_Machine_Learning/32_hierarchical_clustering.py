"""
Hierarchical Clustering - Hierarchical Grouping
================================================
Forms a hierarchy of clusters.
Useful for seeing relationships between groups and subgroups.

Author: Florentino Báez
"""

from sklearn.cluster import AgglomerativeClustering

# Example dataset
X = [[1, 2], [1, 3], [2, 2], [8, 8], [9, 8], [8, 9]]

# Create model
model = AgglomerativeClustering(n_clusters=2)

# Get clusters
labels = model.fit_predict(X)

print("Cluster labels:", labels)
