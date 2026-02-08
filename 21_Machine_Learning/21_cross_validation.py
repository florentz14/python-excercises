"""
Machine Learning - Cross Validation
======================================
Cross Validation provides a more reliable estimate of model performance
than a single train/test split.

Types:
1. K-Fold CV: Split data into K folds, train on K-1, test on 1, rotate
2. Stratified K-Fold: Preserves class proportions in each fold
3. Leave-One-Out (LOO): K = number of samples (expensive)
4. Repeated K-Fold: Repeat K-Fold multiple times
5. Time Series Split: For sequential data (no data leakage)

Why use it?
- Single split can be "lucky" or "unlucky"
- Uses ALL data for both training and testing
- Gives mean and std of performance
"""

import numpy as np
from sklearn.model_selection import (cross_val_score, cross_validate,
                                      KFold, StratifiedKFold,
                                      LeaveOneOut, RepeatedKFold,
                                      TimeSeriesSplit)
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris, load_wine
from sklearn.metrics import make_scorer, accuracy_score, f1_score
import matplotlib.pyplot as plt

# ============================================================
# 1. Basic K-Fold Cross Validation
# ============================================================
print("K-FOLD CROSS VALIDATION")
print("=" * 50)

iris = load_iris()
X, y = iris.data, iris.target

# 5-Fold CV with Decision Tree
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
scores = cross_val_score(dt, X, y, cv=5, scoring="accuracy")

print(f"5-Fold CV scores: {scores.round(4)}")
print(f"Mean accuracy:    {scores.mean():.4f}")
print(f"Std deviation:    {scores.std():.4f}")
print(f"95% CI:           {scores.mean():.4f} ± {scores.std() * 2:.4f}")


# ============================================================
# 2. How K-Fold Works (Visualization)
# ============================================================
print(f"\n{'='*50}")
print("HOW K-FOLD WORKS")
print(f"{'='*50}")

kf = KFold(n_splits=5, shuffle=True, random_state=42)

print(f"Total samples: {len(X)}")
for fold, (train_idx, test_idx) in enumerate(kf.split(X)):
    print(f"  Fold {fold+1}: Train={len(train_idx)} samples, "
          f"Test={len(test_idx)} samples "
          f"(test indices: {test_idx[:5]}...)")

# Visual representation
fig, ax = plt.subplots(figsize=(10, 3))
kf_vis = KFold(n_splits=5)
for fold, (train_idx, test_idx) in enumerate(kf_vis.split(range(20))):
    ax.scatter(train_idx, [fold]*len(train_idx), c="steelblue", s=30, marker="s")
    ax.scatter(test_idx, [fold]*len(test_idx), c="coral", s=30, marker="s")

ax.set_xlabel("Sample Index")
ax.set_ylabel("Fold")
ax.set_title("5-Fold CV (Blue=Train, Red=Test)")
ax.set_yticks(range(5))
ax.set_yticklabels([f"Fold {i+1}" for i in range(5)])
plt.tight_layout()
plt.show()


# ============================================================
# 3. Stratified K-Fold (Preserves Class Distribution)
# ============================================================
print(f"\n{'='*50}")
print("STRATIFIED K-FOLD")
print(f"{'='*50}")

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

scores_strat = cross_val_score(dt, X, y, cv=skf, scoring="accuracy")
print(f"Stratified 5-Fold scores: {scores_strat.round(4)}")
print(f"Mean accuracy:            {scores_strat.mean():.4f}")

# Show class distribution in each fold
print(f"\nClass distribution per fold:")
for fold, (train_idx, test_idx) in enumerate(skf.split(X, y)):
    test_dist = np.bincount(y[test_idx])
    print(f"  Fold {fold+1} test: {dict(zip(iris.target_names, test_dist))}")


# ============================================================
# 4. cross_validate: Multiple Metrics
# ============================================================
print(f"\n{'='*50}")
print("MULTIPLE METRICS WITH cross_validate")
print(f"{'='*50}")

scoring = {
    "accuracy": "accuracy",
    "f1_weighted": "f1_weighted",
    "precision": "precision_weighted",
}

results = cross_validate(dt, X, y, cv=5, scoring=scoring, return_train_score=True)

print(f"{'Metric':<15s} {'Train':>10s} {'Test':>10s}")
print("-" * 38)
for metric in scoring:
    train_key = f"train_{metric}"
    test_key = f"test_{metric}"
    print(f"  {metric:<15s} {results[train_key].mean():>9.4f} {results[test_key].mean():>10.4f}")

print(f"\n  Fit time (avg):   {results['fit_time'].mean():.4f}s")
print(f"  Score time (avg): {results['score_time'].mean():.4f}s")


# ============================================================
# 5. Comparing Models with Cross Validation
# ============================================================
print(f"\n{'='*50}")
print("COMPARING MODELS WITH CV")
print(f"{'='*50}")

models = {
    "Decision Tree":     DecisionTreeClassifier(max_depth=3, random_state=42),
    "Logistic Reg":      LogisticRegression(max_iter=200),
    "Random Forest":     RandomForestClassifier(n_estimators=100, random_state=42),
}

all_scores = {}
print(f"{'Model':<20s} {'Mean':>8s} {'Std':>8s} {'Min':>8s} {'Max':>8s}")
print("-" * 55)

for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=10, scoring="accuracy")
    all_scores[name] = scores
    print(f"  {name:<20s} {scores.mean():>7.4f} {scores.std():>8.4f}"
          f" {scores.min():>8.4f} {scores.max():>8.4f}")

# Box plot comparison
plt.figure(figsize=(8, 5))
plt.boxplot(all_scores.values(), labels=all_scores.keys())
plt.ylabel("Accuracy")
plt.title("Model Comparison (10-Fold CV)")
plt.grid(True, alpha=0.3, axis="y")
plt.tight_layout()
plt.show()


# ============================================================
# 6. Repeated K-Fold and Leave-One-Out
# ============================================================
print(f"\n{'='*50}")
print("REPEATED K-FOLD and LEAVE-ONE-OUT")
print(f"{'='*50}")

# Repeated K-Fold: more stable estimate
rkf = RepeatedKFold(n_splits=5, n_repeats=10, random_state=42)
scores_repeated = cross_val_score(dt, X, y, cv=rkf, scoring="accuracy")
print(f"Repeated 5-Fold (10 repeats):")
print(f"  Mean: {scores_repeated.mean():.4f}, Std: {scores_repeated.std():.4f}")
print(f"  Total evaluations: {len(scores_repeated)}")

# Leave-One-Out (expensive for large datasets)
wine = load_wine()
X_small, y_small = wine.data[:50], wine.target[:50]

loo = LeaveOneOut()
scores_loo = cross_val_score(
    DecisionTreeClassifier(max_depth=3, random_state=42),
    X_small, y_small, cv=loo
)
print(f"\nLeave-One-Out (50 samples):")
print(f"  Mean: {scores_loo.mean():.4f}, Total folds: {len(scores_loo)}")


# ============================================================
# 7. Time Series Cross Validation
# ============================================================
print(f"\n{'='*50}")
print("TIME SERIES CV")
print(f"{'='*50}")

tscv = TimeSeriesSplit(n_splits=5)

print("Time Series Split (respects temporal order):")
for fold, (train_idx, test_idx) in enumerate(tscv.split(range(30))):
    print(f"  Fold {fold+1}: Train={train_idx.tolist()}, Test={test_idx.tolist()}")

print("\nTime Series CV never uses future data for training!")
print("This prevents data leakage in time-dependent problems.")

print("\n--- Cross Validation complete! ---")
