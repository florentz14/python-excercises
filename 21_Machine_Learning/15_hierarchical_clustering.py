"""
Machine Learning - Hierarchical Clustering
=============================================
Hierarchical clustering groups data into a tree of clusters (dendrogram).
It does NOT require specifying the number of clusters in advance.

Two approaches:
1. Agglomerative (bottom-up): Start with each point as its own cluster,
   merge the closest pairs until one cluster remains.
2. Divisive (top-down): Start with one cluster, split until each point
   is its own cluster.

Linkage methods (how to measure distance between clusters):
- Single:   min distance between any two points in different clusters
- Complete: max distance between any two points in different clusters
- Average:  average distance between all pairs of points
- Ward:     minimizes the total within-cluster variance (most common)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs

# ============================================================
# 1. Basic Dendrogram
# ============================================================
print("HIERARCHICAL CLUSTERING - DENDROGRAM")
print("=" * 50)

# Simple 2D data
np.random.seed(42)
X, y_true = make_blobs(n_samples=30, centers=3, cluster_std=1.0, random_state=42)

# Compute linkage matrix
Z = linkage(X, method="ward")

print("Linkage matrix shape:", Z.shape)
print("Each row: [cluster1, cluster2, distance, num_points]")
print(f"First 5 merges:\n{Z[:5].round(3)}")

# Plot dendrogram
plt.figure(figsize=(12, 5))
dendrogram(Z, leaf_rotation=90, leaf_font_size=10)
plt.title("Dendrogram (Ward Linkage)")
plt.xlabel("Sample Index")
plt.ylabel("Distance")
plt.tight_layout()
plt.show()


# ============================================================
# 2. Cutting the Dendrogram to Form Clusters
# ============================================================
print(f"\n{'='*50}")
print("CUTTING THE DENDROGRAM")
print(f"{'='*50}")

# Cut at a distance threshold
labels_dist = fcluster(Z, t=8.0, criterion="distance")
print(f"Cut at distance=8.0: {np.unique(labels_dist).size} clusters")

# Cut to get exactly k clusters
labels_k = fcluster(Z, t=3, criterion="maxclust")
print(f"Cut for k=3 clusters: {np.unique(labels_k)} labels")

# Visualize
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Dendrogram with cut line
dendrogram(Z, ax=axes[0])
axes[0].axhline(y=8.0, color="red", linestyle="--", label="Cut at d=8.0")
axes[0].set_title("Dendrogram with Cut Line")
axes[0].legend()

# Scatter plot of clusters
scatter = axes[1].scatter(X[:, 0], X[:, 1], c=labels_k, cmap="Set1",
                           s=60, edgecolors="black", linewidth=0.5)
axes[1].set_title("3 Clusters from Hierarchical Clustering")
axes[1].set_xlabel("X1")
axes[1].set_ylabel("X2")

plt.tight_layout()
plt.show()


# ============================================================
# 3. Agglomerative Clustering with sklearn
# ============================================================
print(f"\n{'='*50}")
print("AGGLOMERATIVE CLUSTERING (sklearn)")
print(f"{'='*50}")

X_large, y_large = make_blobs(n_samples=200, centers=4, cluster_std=1.2, random_state=42)

agg = AgglomerativeClustering(n_clusters=4, linkage="ward")
labels = agg.fit_predict(X_large)

print(f"Number of clusters: {len(np.unique(labels))}")
print(f"Cluster sizes: {[np.sum(labels == i) for i in range(4)]}")

plt.figure(figsize=(8, 5))
plt.scatter(X_large[:, 0], X_large[:, 1], c=labels, cmap="Set2",
            s=40, edgecolors="black", linewidth=0.5)
plt.title("Agglomerative Clustering (4 Clusters)")
plt.xlabel("X1")
plt.ylabel("X2")
plt.tight_layout()
plt.show()


# ============================================================
# 4. Comparing Linkage Methods
# ============================================================
print(f"\n{'='*50}")
print("COMPARING LINKAGE METHODS")
print(f"{'='*50}")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
methods = ["single", "complete", "average", "ward"]

for ax, method in zip(axes.ravel(), methods):
    Z_m = linkage(X, method=method)
    dendrogram(Z_m, ax=ax, leaf_rotation=90, leaf_font_size=8)
    ax.set_title(f"Linkage: {method.capitalize()}")
    ax.set_xlabel("Sample Index")
    ax.set_ylabel("Distance")

plt.tight_layout()
plt.show()

for method in methods:
    agg_m = AgglomerativeClustering(n_clusters=3, linkage=method)
    labels_m = agg_m.fit_predict(X)
    print(f"  {method:10s} linkage -> Cluster sizes: "
          f"{[np.sum(labels_m == i) for i in range(3)]}")


# ============================================================
# 5. Choosing Number of Clusters
# ============================================================
print(f"\n{'='*50}")
print("CHOOSING NUMBER OF CLUSTERS")
print(f"{'='*50}")

from sklearn.metrics import silhouette_score

scores = []
k_range = range(2, 8)

for k in k_range:
    agg_k = AgglomerativeClustering(n_clusters=k, linkage="ward")
    labels_k = agg_k.fit_predict(X_large)
    score = silhouette_score(X_large, labels_k)
    scores.append(score)
    print(f"  k={k}: Silhouette Score = {score:.4f}")

plt.figure(figsize=(8, 4))
plt.plot(list(k_range), scores, "bo-", linewidth=2, markersize=8)
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Score vs Number of Clusters")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

best_k = list(k_range)[np.argmax(scores)]
print(f"\nBest k = {best_k} (highest silhouette score: {max(scores):.4f})")

print("\n--- Hierarchical Clustering complete! ---")
