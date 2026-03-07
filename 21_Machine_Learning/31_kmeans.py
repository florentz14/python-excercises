"""
K-Means Clustering - Unsupervised Grouping
==========================================
Groups data into K clusters without labels.
Discovers natural groups in the data.

Author: Florentino Báez
"""

from sklearn.cluster import KMeans

# Example dataset (unlabeled)
X = [[1, 2], [1, 3], [2, 2], [8, 8], [9, 8], [8, 9]]

# Create and train model
model = KMeans(n_clusters=2, random_state=42, n_init=10)
model.fit(X)

# Results
print("Cluster labels:", model.labels_)
print("Centroids:", model.cluster_centers_)
