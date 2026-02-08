"""
Machine Learning - Logistic Regression
========================================
Logistic Regression is used for CLASSIFICATION (not regression despite the name).
It predicts the probability that an observation belongs to a class.

Key concepts:
- Uses the sigmoid function: σ(z) = 1 / (1 + e^(-z))
- Output is a probability between 0 and 1
- Threshold (usually 0.5) converts probability to class
- Works for binary and multi-class classification

Use cases: spam detection, disease diagnosis, pass/fail prediction
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, ConfusionMatrixDisplay)

# ============================================================
# 1. The Sigmoid Function
# ============================================================
print("THE SIGMOID FUNCTION")
print("=" * 50)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

z = np.linspace(-10, 10, 200)
plt.figure(figsize=(8, 4))
plt.plot(z, sigmoid(z), "b-", linewidth=2)
plt.axhline(y=0.5, color="red", linestyle="--", alpha=0.7, label="Threshold = 0.5")
plt.axvline(x=0, color="gray", linestyle=":", alpha=0.5)
plt.title("Sigmoid Function")
plt.xlabel("z (linear combination)")
plt.ylabel("σ(z) = Probability")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("σ(-5) =", f"{sigmoid(-5):.4f}  (very likely class 0)")
print("σ( 0) =", f"{sigmoid(0):.4f}  (50/50)")
print("σ( 5) =", f"{sigmoid(5):.4f}  (very likely class 1)")


# ============================================================
# 2. Binary Logistic Regression
# ============================================================
print(f"\n{'='*50}")
print("BINARY LOGISTIC REGRESSION")
print(f"{'='*50}")

# Predict pass/fail based on hours studied
np.random.seed(42)
hours = np.random.uniform(1, 10, 100)
# Probability of passing increases with hours studied
prob_pass = sigmoid(1.5 * hours - 7)
passed = (np.random.random(100) < prob_pass).astype(int)

X = hours.reshape(-1, 1)
y = passed

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

print(f"Coefficient:  {model.coef_[0][0]:.4f}")
print(f"Intercept:    {model.intercept_[0]:.4f}")

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy:     {accuracy:.4f}")

# Visualization
plt.figure(figsize=(10, 5))
plt.scatter(X_train[y_train == 0], y_train[y_train == 0], color="red",
            label="Fail (train)", alpha=0.5, s=40)
plt.scatter(X_train[y_train == 1], y_train[y_train == 1], color="green",
            label="Pass (train)", alpha=0.5, s=40)

x_plot = np.linspace(0, 11, 200).reshape(-1, 1)
y_proba = model.predict_proba(x_plot)[:, 1]
plt.plot(x_plot, y_proba, "b-", linewidth=2, label="P(Pass)")
plt.axhline(y=0.5, color="gray", linestyle="--", alpha=0.5)

plt.title("Logistic Regression: Hours Studied vs Pass/Fail")
plt.xlabel("Hours Studied")
plt.ylabel("Probability of Passing")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ============================================================
# 3. Multi-class Logistic Regression (Iris)
# ============================================================
print(f"\n{'='*50}")
print("MULTI-CLASS LOGISTIC REGRESSION")
print(f"{'='*50}")

from sklearn.datasets import load_iris

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42
)

# Multi-class uses 'multinomial' or 'ovr' (one-vs-rest)
model_multi = LogisticRegression(max_iter=200, multi_class="multinomial")
model_multi.fit(X_train, y_train)

y_pred_iris = model_multi.predict(X_test)
acc = accuracy_score(y_test, y_pred_iris)

print(f"Accuracy: {acc:.4f}")
print(f"\nClassification Report:")
print(classification_report(y_test, y_pred_iris, target_names=iris.target_names))

# Confusion Matrix
plt.figure(figsize=(7, 5))
ConfusionMatrixDisplay.from_predictions(
    y_test, y_pred_iris, display_labels=iris.target_names, cmap="Blues"
)
plt.title("Logistic Regression - Iris Classification")
plt.tight_layout()
plt.show()


# ============================================================
# 4. Probability Predictions
# ============================================================
print(f"{'='*50}")
print("PROBABILITY PREDICTIONS")
print(f"{'='*50}")

# Get probabilities for each class
sample = X_test[:5]
proba = model_multi.predict_proba(sample)

print("Probabilities for first 5 test samples:")
print(f"{'Setosa':>10s} {'Versicolor':>12s} {'Virginica':>12s} {'Predicted':>12s} {'Actual':>8s}")
print("-" * 58)
for i in range(5):
    pred = iris.target_names[model_multi.predict(sample[i:i+1])[0]]
    actual = iris.target_names[y_test[i]]
    print(f"{proba[i][0]:>10.4f} {proba[i][1]:>12.4f} {proba[i][2]:>12.4f}"
          f" {pred:>12s} {actual:>8s}")


# ============================================================
# 5. Regularization in Logistic Regression
# ============================================================
print(f"\n{'='*50}")
print("REGULARIZATION (C parameter)")
print(f"{'='*50}")

print("C controls regularization strength (smaller C = stronger regularization)")
for c_val in [0.01, 0.1, 1.0, 10.0, 100.0]:
    lr = LogisticRegression(C=c_val, max_iter=200)
    lr.fit(X_train, y_train)
    acc_train = accuracy_score(y_train, lr.predict(X_train))
    acc_test = accuracy_score(y_test, lr.predict(X_test))
    print(f"  C={c_val:6.2f} -> Train: {acc_train:.4f}, Test: {acc_test:.4f}")


# ============================================================
# 6. Decision Boundary (2D)
# ============================================================
print(f"\n{'='*50}")
print("DECISION BOUNDARY (2D)")
print(f"{'='*50}")

# Use only 2 features for visualization
X_2d = iris.data[:, :2]  # sepal length, sepal width
X_tr, X_te, y_tr, y_te = train_test_split(X_2d, iris.target, test_size=0.3, random_state=42)

lr_2d = LogisticRegression(max_iter=200)
lr_2d.fit(X_tr, y_tr)

# Create mesh grid for decision boundary
x_min, x_max = X_2d[:, 0].min() - 0.5, X_2d[:, 0].max() + 0.5
y_min, y_max = X_2d[:, 1].min() - 0.5, X_2d[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                      np.linspace(y_min, y_max, 200))

Z = lr_2d.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, alpha=0.3, cmap="Set2")
plt.scatter(X_tr[:, 0], X_tr[:, 1], c=y_tr, cmap="Set1", edgecolors="black",
            s=40, label="Train")
plt.scatter(X_te[:, 0], X_te[:, 1], c=y_te, cmap="Set1", edgecolors="black",
            s=80, marker="^", label="Test")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title(f"Decision Boundary (Test Acc: {accuracy_score(y_te, lr_2d.predict(X_te)):.3f})")
plt.legend()
plt.tight_layout()
plt.show()

print("\n--- Logistic Regression complete! ---")
