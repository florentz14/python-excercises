"""
Machine Learning - K-Nearest Neighbors (KNN)
===============================================
KNN is a simple, instance-based learning algorithm that classifies
a data point based on how its neighbors are classified.

How it works:
1. Choose K (number of neighbors)
2. Calculate the distance from the new point to all training points
3. Select the K nearest neighbors
4. Classification: majority vote of neighbors
5. Regression: average of neighbors' values

Key parameters:
- n_neighbors (K): Number of neighbors to consider
- metric: Distance metric (euclidean, manhattan, minkowski)
- weights: 'uniform' (equal) or 'distance' (closer = more weight)

Important: Feature scaling is CRITICAL for KNN!
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, ConfusionMatrixDisplay)
from sklearn.datasets import load_iris, make_classification

# ============================================================
# 1. Basic KNN Classification
# ============================================================
print("K-NEAREST NEIGHBORS CLASSIFICATION")
print("=" * 50)

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42
)

# Scale features (crucial for distance-based algorithms)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train KNN model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print(f"K = 5")
print(f"Accuracy: {accuracy:.4f}")
print(f"\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))


# ============================================================
# 2. How KNN Works (2D Visualization)
# ============================================================
print(f"{'='*50}")
print("KNN VISUALIZATION (2D)")
print(f"{'='*50}")

# Use only 2 features for visualization
X_2d = iris.data[:, :2]
X_tr, X_te, y_tr, y_te = train_test_split(X_2d, iris.target, test_size=0.3, random_state=42)

sc = StandardScaler()
X_tr_sc = sc.fit_transform(X_tr)
X_te_sc = sc.transform(X_te)

knn_2d = KNeighborsClassifier(n_neighbors=5)
knn_2d.fit(X_tr_sc, y_tr)

# Create decision boundary
x_min, x_max = X_tr_sc[:, 0].min() - 1, X_tr_sc[:, 0].max() + 1
y_min, y_max = X_tr_sc[:, 1].min() - 1, X_tr_sc[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                      np.linspace(y_min, y_max, 200))

Z = knn_2d.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, alpha=0.3, cmap="Set2")
plt.scatter(X_tr_sc[:, 0], X_tr_sc[:, 1], c=y_tr, cmap="Set1",
            edgecolors="black", s=40, label="Train")
plt.scatter(X_te_sc[:, 0], X_te_sc[:, 1], c=y_te, cmap="Set1",
            edgecolors="black", s=80, marker="^", label="Test")
plt.xlabel("Sepal Length (scaled)")
plt.ylabel("Sepal Width (scaled)")
plt.title(f"KNN Decision Boundary (K=5, Acc={accuracy_score(y_te, knn_2d.predict(X_te_sc)):.3f})")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ============================================================
# 3. Finding the Optimal K
# ============================================================
print(f"\n{'='*50}")
print("FINDING THE OPTIMAL K")
print(f"{'='*50}")

k_range = range(1, 31)
train_scores = []
test_scores = []
cv_scores = []

for k in k_range:
    knn_k = KNeighborsClassifier(n_neighbors=k)
    knn_k.fit(X_train_scaled, y_train)
    train_scores.append(accuracy_score(y_train, knn_k.predict(X_train_scaled)))
    test_scores.append(accuracy_score(y_test, knn_k.predict(X_test_scaled)))
    cv = cross_val_score(knn_k, X_train_scaled, y_train, cv=5)
    cv_scores.append(cv.mean())

best_k = list(k_range)[np.argmax(cv_scores)]
print(f"Best K (by CV): {best_k} with CV accuracy: {max(cv_scores):.4f}")

plt.figure(figsize=(10, 5))
plt.plot(list(k_range), train_scores, "b-", label="Training Accuracy", alpha=0.7)
plt.plot(list(k_range), test_scores, "r-", label="Testing Accuracy", alpha=0.7)
plt.plot(list(k_range), cv_scores, "g-", label="CV Accuracy", linewidth=2)
plt.axvline(x=best_k, color="gray", linestyle="--", label=f"Best K={best_k}")
plt.xlabel("K (Number of Neighbors)")
plt.ylabel("Accuracy")
plt.title("KNN: Finding Optimal K")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ============================================================
# 4. Distance Metrics
# ============================================================
print(f"\n{'='*50}")
print("DISTANCE METRICS")
print(f"{'='*50}")

# Euclidean: straight-line distance (default)
# Manhattan: sum of absolute differences (city-block)
# Minkowski: generalization (p=2 -> Euclidean, p=1 -> Manhattan)

point_a = np.array([1, 2])
point_b = np.array([4, 6])

euclidean = np.sqrt(np.sum((point_a - point_b) ** 2))
manhattan = np.sum(np.abs(point_a - point_b))

print(f"Point A: {point_a}, Point B: {point_b}")
print(f"  Euclidean distance: {euclidean:.4f}")
print(f"  Manhattan distance: {manhattan:.4f}")

# Compare metrics
print(f"\nComparing distance metrics on Iris:")
for metric in ["euclidean", "manhattan", "minkowski"]:
    knn_m = KNeighborsClassifier(n_neighbors=5, metric=metric)
    scores_m = cross_val_score(knn_m, X_train_scaled, y_train, cv=5)
    print(f"  {metric:15s}: CV accuracy = {scores_m.mean():.4f}")


# ============================================================
# 5. Weighted KNN
# ============================================================
print(f"\n{'='*50}")
print("WEIGHTED KNN")
print(f"{'='*50}")

# Uniform: all neighbors have equal vote
knn_uniform = KNeighborsClassifier(n_neighbors=10, weights="uniform")
knn_uniform.fit(X_train_scaled, y_train)
acc_uniform = accuracy_score(y_test, knn_uniform.predict(X_test_scaled))

# Distance: closer neighbors have more influence
knn_distance = KNeighborsClassifier(n_neighbors=10, weights="distance")
knn_distance.fit(X_train_scaled, y_train)
acc_distance = accuracy_score(y_test, knn_distance.predict(X_test_scaled))

print(f"K=10, Uniform weights:  {acc_uniform:.4f}")
print(f"K=10, Distance weights: {acc_distance:.4f}")
print("\nDistance weighting is useful when K is large")


# ============================================================
# 6. KNN for Regression
# ============================================================
print(f"\n{'='*50}")
print("KNN REGRESSION")
print(f"{'='*50}")

np.random.seed(42)
X_reg = np.sort(5 * np.random.rand(100, 1), axis=0)
y_reg = np.sin(X_reg).ravel() + np.random.normal(0, 0.15, 100)

X_tr_r, X_te_r, y_tr_r, y_te_r = train_test_split(X_reg, y_reg, test_size=0.3, random_state=42)

x_plot = np.linspace(0, 5, 200).reshape(-1, 1)

plt.figure(figsize=(12, 4))
for i, k in enumerate([1, 5, 20]):
    knn_reg = KNeighborsRegressor(n_neighbors=k)
    knn_reg.fit(X_tr_r, y_tr_r)
    y_plot = knn_reg.predict(x_plot)
    from sklearn.metrics import r2_score
    r2 = r2_score(y_te_r, knn_reg.predict(X_te_r))

    plt.subplot(1, 3, i + 1)
    plt.scatter(X_reg, y_reg, c="steelblue", s=15, alpha=0.5)
    plt.plot(x_plot, y_plot, "r-", linewidth=2)
    plt.title(f"K={k}, R²={r2:.3f}")
    plt.grid(True, alpha=0.3)

plt.suptitle("KNN Regression", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()

print("K=1:  Overfitting (too sensitive to individual points)")
print("K=5:  Good balance")
print("K=20: Underfitting (too smooth)")


# ============================================================
# 7. KNN Pros and Cons
# ============================================================
print(f"\n{'='*50}")
print("KNN: PROS AND CONS")
print(f"{'='*50}")

print("""
PROS:
  + Simple and intuitive (no training phase)
  + Works for both classification and regression
  + No assumptions about data distribution
  + Adapts to complex decision boundaries

CONS:
  - Slow prediction on large datasets (computes distances to all points)
  - Sensitive to feature scaling (MUST scale features!)
  - Sensitive to irrelevant features
  - Curse of dimensionality (struggles with many features)
  - Must store entire training dataset (memory intensive)

TIPS:
  - Always scale/normalize features
  - Use cross-validation to find optimal K
  - Use odd K for binary classification (avoids ties)
  - Consider dimensionality reduction (PCA) for high-dimensional data
""")

print("--- K-Nearest Neighbors complete! ---")
