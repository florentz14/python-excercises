"""
Machine Learning - K-Means Clustering
========================================
K-Means is an unsupervised learning algorithm that groups data
into K clusters based on similarity (distance).

How it works:
1. Choose K (number of clusters)
2. Randomly place K centroids
3. Assign each data point to the nearest centroid
4. Recalculate centroids as the mean of assigned points
5. Repeat steps 3-4 until convergence

Key parameters:
- n_clusters (K): Number of clusters
- init: Initialization method ('k-means++' is best)
- n_init: Number of times to run with different seeds
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# ============================================================
# 1. Basic K-Means Clustering
# ============================================================
print("BASIC K-MEANS CLUSTERING")
print("=" * 50)

# Generate sample data with 4 clusters
np.random.seed(42)
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.8, random_state=42)

# Apply K-Means with K=4
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
labels = kmeans.fit_predict(X)
centroids = kmeans.cluster_centers_

print(f"Number of clusters: {kmeans.n_clusters}")
print(f"Centroids:\n{centroids.round(3)}")
print(f"Inertia (within-cluster sum of squares): {kmeans.inertia_:.2f}")
print(f"Iterations to converge: {kmeans.n_iter_}")

# Visualize
plt.figure(figsize=(8, 6))
scatter = plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="Set2",
                      s=40, edgecolors="black", linewidth=0.5, alpha=0.7)
plt.scatter(centroids[:, 0], centroids[:, 1], c="red", marker="X",
            s=200, edgecolors="black", linewidth=2, label="Centroids")
plt.title("K-Means Clustering (K=4)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ============================================================
# 2. The Elbow Method (Choosing K)
# ============================================================
print(f"\n{'='*50}")
print("ELBOW METHOD - CHOOSING K")
print(f"{'='*50}")

inertias = []
k_range = range(1, 11)

for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X)
    inertias.append(km.inertia_)
    if k <= 6:
        print(f"  K={k}: Inertia = {km.inertia_:.2f}")

plt.figure(figsize=(8, 5))
plt.plot(list(k_range), inertias, "bo-", linewidth=2, markersize=8)
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia (WCSS)")
plt.title("Elbow Method")
plt.grid(True, alpha=0.3)
plt.annotate("Elbow point", xy=(4, inertias[3]), fontsize=12,
             arrowprops=dict(arrowstyle="->", color="red"),
             xytext=(6, inertias[3] + 200), color="red")
plt.tight_layout()
plt.show()

print("Look for the 'elbow' - where inertia stops decreasing rapidly")


# ============================================================
# 3. Silhouette Score
# ============================================================
print(f"\n{'='*50}")
print("SILHOUETTE SCORE")
print(f"{'='*50}")

print("Silhouette Score: How similar a point is to its own cluster")
print("vs other clusters. Range: -1 (wrong cluster) to 1 (perfect)")

sil_scores = []
for k in range(2, 8):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels_k = km.fit_predict(X)
    sil = silhouette_score(X, labels_k)
    sil_scores.append(sil)
    print(f"  K={k}: Silhouette = {sil:.4f}")

best_k = np.argmax(sil_scores) + 2
print(f"\nBest K = {best_k} (highest silhouette score)")


# ============================================================
# 4. Step-by-Step K-Means Visualization
# ============================================================
print(f"\n{'='*50}")
print("K-MEANS STEP BY STEP")
print(f"{'='*50}")

# Visualize the iterative process
from sklearn.cluster import KMeans

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
X_small, _ = make_blobs(n_samples=100, centers=3, cluster_std=1.5, random_state=42)

for i, ax in enumerate(axes.ravel()):
    if i == 0:
        ax.scatter(X_small[:, 0], X_small[:, 1], c="gray", s=30, alpha=0.5)
        ax.set_title("Step 0: Original Data")
    else:
        km = KMeans(n_clusters=3, max_iter=i, n_init=1, random_state=42)
        km.fit(X_small)
        ax.scatter(X_small[:, 0], X_small[:, 1], c=km.labels_, cmap="Set2",
                   s=30, edgecolors="black", linewidth=0.3, alpha=0.7)
        ax.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],
                   c="red", marker="X", s=150, edgecolors="black", linewidth=2)
        ax.set_title(f"Step {i}: Iteration {i}")
    ax.grid(True, alpha=0.3)

plt.suptitle("K-Means Convergence", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()


# ============================================================
# 5. K-Means with Real-World Scenario
# ============================================================
print(f"\n{'='*50}")
print("CUSTOMER SEGMENTATION EXAMPLE")
print(f"{'='*50}")

np.random.seed(42)
n_customers = 200

# Customer features: Annual Income ($k) and Spending Score (1-100)
income = np.concatenate([
    np.random.normal(30, 8, 50),
    np.random.normal(50, 10, 60),
    np.random.normal(80, 8, 40),
    np.random.normal(70, 10, 50),
])[:n_customers]

spending = np.concatenate([
    np.random.normal(30, 10, 50),
    np.random.normal(70, 12, 60),
    np.random.normal(20, 8, 40),
    np.random.normal(80, 10, 50),
])[:n_customers]

X_customers = np.column_stack([income, spending])

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_customers)

# Find optimal K
best_sil = -1
for k in range(2, 8):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels_k = km.fit_predict(X_scaled)
    sil = silhouette_score(X_scaled, labels_k)
    if sil > best_sil:
        best_sil = sil
        best_k = k

print(f"Optimal K: {best_k} (silhouette: {best_sil:.4f})")

# Final clustering
km_final = KMeans(n_clusters=best_k, random_state=42, n_init=10)
cust_labels = km_final.fit_predict(X_scaled)

plt.figure(figsize=(8, 6))
for i in range(best_k):
    mask = cust_labels == i
    plt.scatter(income[mask], spending[mask], s=40, alpha=0.7,
                edgecolors="black", linewidth=0.3, label=f"Segment {i+1}")

plt.xlabel("Annual Income ($k)")
plt.ylabel("Spending Score")
plt.title(f"Customer Segmentation (K={best_k})")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Segment analysis
for i in range(best_k):
    mask = cust_labels == i
    print(f"  Segment {i+1}: {mask.sum()} customers | "
          f"Avg Income: ${income[mask].mean():.0f}k | "
          f"Avg Spending: {spending[mask].mean():.0f}")


# ============================================================
# 6. K-Means Limitations
# ============================================================
print(f"\n{'='*50}")
print("K-MEANS LIMITATIONS")
print(f"{'='*50}")

print("""
Limitations of K-Means:
1. Must specify K in advance
2. Assumes spherical, equally-sized clusters
3. Sensitive to initialization (use k-means++)
4. Sensitive to outliers
5. Struggles with non-convex shapes (e.g., circles within circles)

Alternatives:
- DBSCAN: No need to specify K, handles non-convex shapes
- Hierarchical: No K needed, provides dendrogram
- Gaussian Mixture: Handles elliptical clusters
""")

print("\n--- K-Means Clustering complete! ---")
