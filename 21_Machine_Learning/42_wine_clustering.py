"""
ML Mini Course - Step 4: Clustering with real dataset
======================================================
Cluster wines (red/white) without using the label.
Dataset: wine_quality.csv

Author: Florentino Báez
"""

import os
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, accuracy_score

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "09_Pandas", "data")


def main():
    # 1. Load data
    path = os.path.join(DATA_DIR, "wine_quality.csv")
    df = pd.read_csv(path)

    # 2. Clean NaN
    df = df.dropna()

    # 3. Numeric features (exclude wine_type for unsupervised clustering)
    feature_cols = ["fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar", "alcohol", "quality", "pH"]
    X = df[feature_cols]

    # 4. Scale (K-Means is sensitive to scale)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 5. K-Means with k=2 (red vs white)
    model = KMeans(n_clusters=2, random_state=42, n_init=10)
    clusters = model.fit_predict(X_scaled)

    # 6. Compare with real label (for evaluation only)
    le = LabelEncoder()
    y_real = le.fit_transform(df["wine_type"])

    # Approximate match (clusters may be inverted)
    if accuracy_score(y_real, clusters) < 0.5:
        clusters = 1 - clusters
    acc = accuracy_score(y_real, clusters)

    silhouette = silhouette_score(X_scaled, clusters)

    print("=" * 50)
    print("CLUSTERING - Wines (K-Means)")
    print("=" * 50)
    print(f"\nClusters found: {model.n_clusters}")
    print(f"Match with real type (red/white): {acc:.2%}")
    print(f"Silhouette score: {silhouette:.4f}")
    print(f"\nCentroids (first 3 dimensions):")
    print(model.cluster_centers_[:, :3])
    print("\n[OK] Clustering completed.")


if __name__ == "__main__":
    main()
