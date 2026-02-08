"""
Machine Learning - Bootstrap Aggregation (Bagging)
====================================================
Bootstrap Aggregation (Bagging) is an ensemble method that improves
model accuracy and reduces overfitting.

How it works:
1. Create multiple bootstrap samples (random samples WITH replacement)
2. Train a separate model on each bootstrap sample
3. Combine predictions:
   - Classification: majority vote
   - Regression: average of predictions

Key benefits:
- Reduces variance (overfitting)
- Works well with unstable models (Decision Trees)
- Random Forest = Bagging + feature randomization

Key term: OOB (Out-of-Bag) score - each bootstrap sample leaves out ~37%
of data, which can be used for validation without a separate test set.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import BaggingClassifier, BaggingRegressor, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, r2_score
from sklearn.datasets import load_iris, make_classification

# ============================================================
# 1. Bootstrap Sampling Explained
# ============================================================
print("BOOTSTRAP SAMPLING")
print("=" * 50)

np.random.seed(42)
original_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(f"Original data: {original_data}")
print(f"\nBootstrap samples (same size, WITH replacement):")
for i in range(5):
    sample = np.random.choice(original_data, size=len(original_data), replace=True)
    not_in = set(original_data) - set(sample)
    print(f"  Sample {i+1}: {sample}  | Out-of-bag: {not_in}")

# Probability that a sample is NOT picked in n draws: (1 - 1/n)^n ≈ e^-1 ≈ 0.368
print(f"\nExpected OOB fraction: ~{1/np.e:.1%} ({1/np.e*100:.1f}% not in each sample)")


# ============================================================
# 2. Bagging Classifier
# ============================================================
print(f"\n{'='*50}")
print("BAGGING CLASSIFIER")
print(f"{'='*50}")

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42
)

# Single Decision Tree vs Bagging
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)
dt_acc = accuracy_score(y_test, dt.predict(X_test))

bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=100,       # Number of trees
    max_samples=0.8,        # % of samples per bootstrap
    max_features=1.0,       # % of features per tree
    oob_score=True,         # Calculate OOB score
    random_state=42,
    n_jobs=-1
)
bagging.fit(X_train, y_train)
bag_acc = accuracy_score(y_test, bagging.predict(X_test))

print(f"Single Decision Tree accuracy: {dt_acc:.4f}")
print(f"Bagging (100 trees) accuracy:  {bag_acc:.4f}")
print(f"OOB score:                     {bagging.oob_score_:.4f}")
print(f"Improvement:                   {(bag_acc - dt_acc)*100:+.1f}%")


# ============================================================
# 3. Effect of Number of Estimators
# ============================================================
print(f"\n{'='*50}")
print("EFFECT OF NUMBER OF ESTIMATORS")
print(f"{'='*50}")

n_estimators_range = [1, 5, 10, 25, 50, 100, 200, 500]
accuracies = []

for n in n_estimators_range:
    bag = BaggingClassifier(
        estimator=DecisionTreeClassifier(),
        n_estimators=n, random_state=42, n_jobs=-1
    )
    bag.fit(X_train, y_train)
    acc = accuracy_score(y_test, bag.predict(X_test))
    accuracies.append(acc)
    print(f"  n_estimators={n:3d}: accuracy = {acc:.4f}")

plt.figure(figsize=(8, 5))
plt.plot(n_estimators_range, accuracies, "bo-", linewidth=2, markersize=8)
plt.xlabel("Number of Estimators")
plt.ylabel("Test Accuracy")
plt.title("Bagging: Accuracy vs Number of Estimators")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ============================================================
# 4. Random Forest (Bagging + Feature Randomization)
# ============================================================
print(f"\n{'='*50}")
print("RANDOM FOREST")
print(f"{'='*50}")

# Random Forest adds feature randomization to bagging
rf = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    max_features="sqrt",    # Random subset of features at each split
    oob_score=True,
    random_state=42,
    n_jobs=-1
)
rf.fit(X_train, y_train)
rf_acc = accuracy_score(y_test, rf.predict(X_test))

print(f"Random Forest accuracy: {rf_acc:.4f}")
print(f"OOB score:              {rf.oob_score_:.4f}")

# Feature importance
print(f"\nFeature Importance:")
for name, imp in zip(iris.feature_names, rf.feature_importances_):
    bar = "█" * int(imp * 40)
    print(f"  {name:20s}: {imp:.4f} {bar}")


# ============================================================
# 5. Bagging vs Single Model Comparison
# ============================================================
print(f"\n{'='*50}")
print("COMPARISON: SINGLE TREE vs BAGGING vs RANDOM FOREST")
print(f"{'='*50}")

X_clf, y_clf = make_classification(
    n_samples=500, n_features=20, n_informative=10,
    n_redundant=5, random_state=42
)
X_tr, X_te, y_tr, y_te = train_test_split(X_clf, y_clf, test_size=0.3, random_state=42)

models = {
    "Decision Tree":   DecisionTreeClassifier(random_state=42),
    "Bagging (DT)":    BaggingClassifier(n_estimators=100, random_state=42),
    "Random Forest":   RandomForestClassifier(n_estimators=100, random_state=42),
}

print(f"{'Model':<20s} {'Train':>8s} {'Test':>8s} {'CV Mean':>8s}")
print("-" * 48)

for name, model in models.items():
    model.fit(X_tr, y_tr)
    train_acc = accuracy_score(y_tr, model.predict(X_tr))
    test_acc = accuracy_score(y_te, model.predict(X_te))
    cv = cross_val_score(model, X_clf, y_clf, cv=5)
    print(f"  {name:<20s} {train_acc:>7.4f} {test_acc:>8.4f} {cv.mean():>8.4f}")


# ============================================================
# 6. Bagging for Regression
# ============================================================
print(f"\n{'='*50}")
print("BAGGING REGRESSOR")
print(f"{'='*50}")

np.random.seed(42)
X_reg = np.sort(5 * np.random.rand(100, 1), axis=0)
y_reg = np.sin(X_reg).ravel() + np.random.normal(0, 0.15, 100)

X_tr_r, X_te_r, y_tr_r, y_te_r = train_test_split(X_reg, y_reg, test_size=0.3, random_state=42)

dt_reg = DecisionTreeRegressor(random_state=42)
dt_reg.fit(X_tr_r, y_tr_r)

bag_reg = BaggingRegressor(n_estimators=100, random_state=42)
bag_reg.fit(X_tr_r, y_tr_r)

dt_r2 = r2_score(y_te_r, dt_reg.predict(X_te_r))
bag_r2 = r2_score(y_te_r, bag_reg.predict(X_te_r))

print(f"Single Decision Tree R²: {dt_r2:.4f}")
print(f"Bagging Regressor R²:    {bag_r2:.4f}")

x_plot = np.linspace(0, 5, 200).reshape(-1, 1)

plt.figure(figsize=(10, 5))
plt.scatter(X_reg, y_reg, c="steelblue", s=20, alpha=0.5, label="Data")
plt.plot(x_plot, dt_reg.predict(x_plot), "g-", linewidth=2, label=f"Single Tree (R²={dt_r2:.3f})")
plt.plot(x_plot, bag_reg.predict(x_plot), "r-", linewidth=2, label=f"Bagging (R²={bag_r2:.3f})")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Bagging vs Single Tree (Regression)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\n--- Bootstrap Aggregation complete! ---")
