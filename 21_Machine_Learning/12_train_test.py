"""
Machine Learning - Train/Test Split
=====================================
To evaluate an ML model, we split data into:
- Training set: Used to TRAIN the model (typically 80%)
- Testing set:  Used to EVALUATE the model (typically 20%)

This tells us how well the model generalizes to unseen data.

Why split?
- If we evaluate on training data, we only see how well it memorizes
- Testing on unseen data shows true predictive performance
- Helps detect overfitting
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# ============================================================
# 1. Basic Train/Test Split
# ============================================================
np.random.seed(2)
x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x

print("BASIC TRAIN/TEST SPLIT")
print("=" * 50)
print(f"Total samples: {len(x)}")

# Split: 80% training, 20% testing
X = x.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training samples: {len(X_train)} ({len(X_train)/len(x)*100:.0f}%)")
print(f"Testing samples:  {len(X_test)} ({len(X_test)/len(x)*100:.0f}%)")


# ============================================================
# 2. Train and Evaluate
# ============================================================
print(f"\n{'='*50}")
print("TRAIN AND EVALUATE")
print(f"{'='*50}")

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Use polynomial regression (degree 4) for curved data
model = make_pipeline(PolynomialFeatures(degree=4), LinearRegression())
model.fit(X_train, y_train)

# Score on training data
train_pred = model.predict(X_train)
train_r2 = r2_score(y_train, train_pred)
train_rmse = np.sqrt(mean_squared_error(y_train, train_pred))

# Score on test data
test_pred = model.predict(X_test)
test_r2 = r2_score(y_test, test_pred)
test_rmse = np.sqrt(mean_squared_error(y_test, test_pred))

print(f"Training R²:  {train_r2:.4f}")
print(f"Testing R²:   {test_r2:.4f}")
print(f"Training RMSE: {train_rmse:.2f}")
print(f"Testing RMSE:  {test_rmse:.2f}")

# Visualization
plt.figure(figsize=(10, 5))
plt.scatter(X_train, y_train, color="steelblue", alpha=0.6, label="Training data")
plt.scatter(X_test, y_test, color="coral", alpha=0.8, s=80, edgecolors="black",
            label="Testing data")

x_line = np.linspace(X.min(), X.max(), 200).reshape(-1, 1)
y_line = model.predict(x_line)
plt.plot(x_line, y_line, "r-", linewidth=2, label=f"Model (R²={test_r2:.3f})")

plt.title("Train/Test Split Visualization")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ============================================================
# 3. Different Test Sizes
# ============================================================
print(f"\n{'='*50}")
print("DIFFERENT TEST SIZES")
print(f"{'='*50}")

for test_size in [0.1, 0.2, 0.3, 0.4, 0.5]:
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=test_size, random_state=42)
    m = make_pipeline(PolynomialFeatures(degree=4), LinearRegression())
    m.fit(X_tr, y_tr)
    r2_tr = r2_score(y_tr, m.predict(X_tr))
    r2_te = r2_score(y_te, m.predict(X_te))
    print(f"  Test size: {test_size:.0%} -> Train R²: {r2_tr:.4f}, Test R²: {r2_te:.4f}"
          f" (Train: {len(X_tr)}, Test: {len(X_te)})")


# ============================================================
# 4. Random State and Reproducibility
# ============================================================
print(f"\n{'='*50}")
print("RANDOM STATE")
print(f"{'='*50}")

print("Different random_state = different splits:")
for rs in [0, 1, 42, 100]:
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=rs)
    m = make_pipeline(PolynomialFeatures(degree=4), LinearRegression())
    m.fit(X_tr, y_tr)
    r2 = r2_score(y_te, m.predict(X_te))
    print(f"  random_state={rs:3d} -> Test R² = {r2:.4f}")

print("\nSame random_state = SAME split (reproducible)")


# ============================================================
# 5. Stratified Split (for classification)
# ============================================================
print(f"\n{'='*50}")
print("STRATIFIED SPLIT (Classification)")
print(f"{'='*50}")

from sklearn.datasets import make_classification

X_clf, y_clf = make_classification(n_samples=100, n_features=5,
                                    n_classes=2, weights=[0.7, 0.3],
                                    random_state=42)

# Regular split (may not preserve class proportions)
X_tr_r, X_te_r, y_tr_r, y_te_r = train_test_split(
    X_clf, y_clf, test_size=0.2, random_state=42
)

# Stratified split (preserves class proportions)
X_tr_s, X_te_s, y_tr_s, y_te_s = train_test_split(
    X_clf, y_clf, test_size=0.2, random_state=42, stratify=y_clf
)

print(f"Original class distribution: {np.bincount(y_clf) / len(y_clf)}")
print(f"Regular split (test):        {np.bincount(y_te_r) / len(y_te_r)}")
print(f"Stratified split (test):     {np.bincount(y_te_s) / len(y_te_s)}")
print("\nStratified split preserves the original class proportions!")


# ============================================================
# 6. Overfitting Detection with Train/Test
# ============================================================
print(f"\n{'='*50}")
print("OVERFITTING DETECTION")
print(f"{'='*50}")

degrees = range(1, 16)
train_scores = []
test_scores = []

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

for d in degrees:
    m = make_pipeline(PolynomialFeatures(degree=d), LinearRegression())
    m.fit(X_tr, y_tr)
    tr_score = r2_score(y_tr, m.predict(X_tr))
    te_score = r2_score(y_te, np.clip(m.predict(X_te), -200, 200))
    train_scores.append(tr_score)
    test_scores.append(te_score)

plt.figure(figsize=(10, 5))
plt.plot(list(degrees), train_scores, "bo-", label="Training R²")
plt.plot(list(degrees), test_scores, "ro-", label="Testing R²")
plt.xlabel("Polynomial Degree")
plt.ylabel("R² Score")
plt.title("Overfitting Detection: Train vs Test Performance")
plt.legend()
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color="gray", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

print("When train R² keeps going up but test R² drops -> OVERFITTING")
print("Best model: highest test R² (not highest train R²)")

print("\n--- Train/Test Split complete! ---")
