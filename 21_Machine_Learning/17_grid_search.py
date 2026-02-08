"""
Machine Learning - Grid Search
=================================
Grid Search systematically works through multiple combinations of
hyperparameters, cross-validating each to find the optimal settings.

Hyperparameters: Settings that are NOT learned from data but set before training.
Examples: max_depth in Decision Tree, C in Logistic Regression, k in KNN

Grid Search process:
1. Define a grid of hyperparameter values to try
2. Train a model for EVERY combination
3. Evaluate each using cross-validation
4. Return the combination with the best score

Alternative: RandomizedSearchCV (faster, samples random combinations)
"""

import numpy as np
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import warnings
warnings.filterwarnings("ignore")

# ============================================================
# 1. Basic Grid Search with Decision Tree
# ============================================================
print("GRID SEARCH - DECISION TREE")
print("=" * 50)

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42
)

# Define the parameter grid
param_grid_dt = {
    "max_depth": [1, 2, 3, 4, 5, 10, None],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4],
    "criterion": ["gini", "entropy"],
}

total_combinations = 1
for v in param_grid_dt.values():
    total_combinations *= len(v)
print(f"Total combinations to try: {total_combinations}")

# Run Grid Search with 5-fold cross-validation
grid_search_dt = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid_dt,
    cv=5,
    scoring="accuracy",
    n_jobs=-1,       # Use all CPU cores
    verbose=0
)
grid_search_dt.fit(X_train, y_train)

print(f"\nBest parameters: {grid_search_dt.best_params_}")
print(f"Best CV score:   {grid_search_dt.best_score_:.4f}")

# Evaluate on test set
best_dt = grid_search_dt.best_estimator_
test_acc = accuracy_score(y_test, best_dt.predict(X_test))
print(f"Test accuracy:   {test_acc:.4f}")


# ============================================================
# 2. Viewing All Results
# ============================================================
print(f"\n{'='*50}")
print("TOP 10 RESULTS")
print(f"{'='*50}")

import pandas as pd

results = pd.DataFrame(grid_search_dt.cv_results_)
results = results.sort_values("rank_test_score")
cols = ["rank_test_score", "mean_test_score", "std_test_score", "params"]
print(results[cols].head(10).to_string(index=False))


# ============================================================
# 3. Grid Search with SVM
# ============================================================
print(f"\n{'='*50}")
print("GRID SEARCH - SVM")
print(f"{'='*50}")

param_grid_svm = {
    "C": [0.1, 1, 10, 100],
    "kernel": ["linear", "rbf", "poly"],
    "gamma": ["scale", "auto"],
}

grid_search_svm = GridSearchCV(
    SVC(random_state=42),
    param_grid_svm,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)
grid_search_svm.fit(X_train, y_train)

print(f"Best parameters: {grid_search_svm.best_params_}")
print(f"Best CV score:   {grid_search_svm.best_score_:.4f}")
print(f"Test accuracy:   {accuracy_score(y_test, grid_search_svm.best_estimator_.predict(X_test)):.4f}")


# ============================================================
# 4. Randomized Search (Faster Alternative)
# ============================================================
print(f"\n{'='*50}")
print("RANDOMIZED SEARCH")
print(f"{'='*50}")

from scipy.stats import randint, uniform

param_distributions = {
    "n_estimators": randint(50, 300),
    "max_depth": [3, 5, 10, 15, None],
    "min_samples_split": randint(2, 20),
    "min_samples_leaf": randint(1, 10),
    "max_features": ["sqrt", "log2", None],
}

random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_distributions,
    n_iter=50,          # Try 50 random combinations (not all)
    cv=5,
    scoring="accuracy",
    random_state=42,
    n_jobs=-1
)
random_search.fit(X_train, y_train)

print(f"Best parameters: {random_search.best_params_}")
print(f"Best CV score:   {random_search.best_score_:.4f}")
print(f"Test accuracy:   {accuracy_score(y_test, random_search.best_estimator_.predict(X_test)):.4f}")


# ============================================================
# 5. Multiple Scoring Metrics
# ============================================================
print(f"\n{'='*50}")
print("MULTIPLE SCORING METRICS")
print(f"{'='*50}")

grid_multi = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    {"max_depth": [2, 3, 4, 5], "criterion": ["gini", "entropy"]},
    cv=5,
    scoring=["accuracy", "f1_weighted", "precision_weighted"],
    refit="accuracy",  # Use accuracy to select the best model
    n_jobs=-1
)
grid_multi.fit(X_train, y_train)

results_multi = pd.DataFrame(grid_multi.cv_results_)
cols_multi = ["params", "mean_test_accuracy", "mean_test_f1_weighted",
              "mean_test_precision_weighted"]
print(results_multi[cols_multi].round(4).to_string(index=False))


# ============================================================
# 6. Visualization: Grid Search Results
# ============================================================
import matplotlib.pyplot as plt

# Heatmap of Grid Search results (SVM example)
results_svm = pd.DataFrame(grid_search_svm.cv_results_)

plt.figure(figsize=(10, 5))
for kernel in ["linear", "rbf", "poly"]:
    mask = results_svm["param_kernel"] == kernel
    subset = results_svm[mask]
    c_values = subset["param_C"].astype(float)
    scores = subset["mean_test_score"]
    plt.plot(c_values, scores, "o-", label=f"kernel={kernel}", markersize=8)

plt.xscale("log")
plt.xlabel("C (regularization)")
plt.ylabel("Mean CV Accuracy")
plt.title("Grid Search Results: SVM")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\n--- Grid Search complete! ---")
