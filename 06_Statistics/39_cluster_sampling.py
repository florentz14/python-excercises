# -------------------------------------------------
# File Name: 39_cluster_sampling.py
# Description: Muestreo por conglomerados.
# -------------------------------------------------

import numpy as np

np.random.seed(42)
# 10 clusters (e.g. schools), each with different number of students
clusters = [
    np.random.normal(70, 10, 30),
    np.random.normal(72, 12, 25),
    np.random.normal(68, 8, 40),
    np.random.normal(75, 15, 20),
    np.random.normal(69, 10, 35),
    np.random.normal(71, 11, 28),
    np.random.normal(73, 9, 22),
    np.random.normal(70, 10, 38),
    np.random.normal(72, 12, 26),
    np.random.normal(68, 10, 32),
]

# Select 3 clusters at random, use all elements
n_clusters = 3
selected_idx = np.random.choice(len(clusters), n_clusters, replace=False)
cluster_sample = np.concatenate([clusters[i] for i in selected_idx])

print("=== CLUSTER SAMPLING ===")
print(f"Total clusters: {len(clusters)}")
print(f"Clusters selected: {n_clusters}")
print(f"Cluster sample mean: {np.mean(cluster_sample):.2f}")
print(f"Cluster sample size: {len(cluster_sample)}")
