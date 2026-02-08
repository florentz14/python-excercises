"""
Machine Learning - Decision Tree
==================================
A Decision Tree makes predictions by learning simple decision rules
from data features. It works for both classification and regression.

How it works:
1. Picks the best feature to split the data
2. Splits into branches based on feature values
3. Repeats until a stopping condition is met
4. Leaf nodes contain the final predictions

Key terms:
- Root node: Top of the tree (first split)
- Internal node: Decision point
- Leaf node: Final prediction
- Depth: Number of levels in the tree
- Gini impurity / Entropy: Measures how "mixed" a node is
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.tree import export_text, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# ============================================================
# 1. Decision Tree Classification
# ============================================================
print("DECISION TREE CLASSIFICATION")
print("=" * 50)

# Should a person go to a comedy show?
# Features: Age, Experience, Rank, Nationality (encoded)
data = {
    "Age":         [36, 42, 23, 52, 43, 44, 66, 35, 52, 35, 24, 18, 45],
    "Experience":  [10, 12,  4, 14, 14, 14,  5, 10, 20,  5,  2,  1, 16],
    "Rank":        [ 9,  4,  6,  4,  8,  5,  7,  9,  7,  5,  7,  3,  8],
    "Nationality": [ 0,  0,  1,  1,  0,  1,  0,  1,  0,  0,  1,  1,  0],
    "Go":          [ 1,  0,  0,  0,  1,  0,  1,  1,  1,  0,  0,  0,  1],
}

X = np.array([data["Age"], data["Experience"], data["Rank"], data["Nationality"]]).T
y = np.array(data["Go"])

# Create and train the Decision Tree
dtree = DecisionTreeClassifier(max_depth=3, random_state=42)
dtree.fit(X, y)

# Print the tree as text
feature_names = ["Age", "Experience", "Rank", "Nationality"]
tree_text = export_text(dtree, feature_names=feature_names)
print("\nDecision Tree Structure:")
print(tree_text)


# ============================================================
# 2. Visualizing the Tree
# ============================================================
plt.figure(figsize=(14, 8))
plot_tree(dtree, feature_names=feature_names, class_names=["No", "Yes"],
          filled=True, rounded=True, fontsize=10)
plt.title("Decision Tree: Should I Go to the Comedy Show?")
plt.tight_layout()
plt.show()


# ============================================================
# 3. Making Predictions
# ============================================================
print(f"\n{'='*50}")
print("PREDICTIONS")
print(f"{'='*50}")

# Predict: 40-year-old, 10 years experience, rank 7, nationality=1
new_person = np.array([[40, 10, 7, 1]])
prediction = dtree.predict(new_person)
proba = dtree.predict_proba(new_person)

print(f"Person: Age=40, Exp=10, Rank=7, Nat=1")
print(f"Prediction: {'GO' if prediction[0] == 1 else 'STAY'}")
print(f"Probability: No={proba[0][0]:.2f}, Yes={proba[0][1]:.2f}")


# ============================================================
# 4. Decision Tree with Iris Dataset
# ============================================================
print(f"\n{'='*50}")
print("IRIS DATASET EXAMPLE")
print(f"{'='*50}")

from sklearn.datasets import load_iris

iris = load_iris()
X_iris = iris.data
y_iris = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X_iris, y_iris, test_size=0.3, random_state=42
)

# Train with different depths
for depth in [1, 2, 3, 5, None]:
    dt = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt.fit(X_train, y_train)
    train_acc = accuracy_score(y_train, dt.predict(X_train))
    test_acc = accuracy_score(y_test, dt.predict(X_test))
    depth_str = str(depth) if depth else "None"
    print(f"  Depth={depth_str:4s}: Train={train_acc:.3f}, Test={test_acc:.3f}")

# Best model
best_dt = DecisionTreeClassifier(max_depth=3, random_state=42)
best_dt.fit(X_train, y_train)
y_pred = best_dt.predict(X_test)

print(f"\nClassification Report (depth=3):")
print(classification_report(y_test, y_pred, target_names=iris.target_names))


# ============================================================
# 5. Feature Importance
# ============================================================
print(f"{'='*50}")
print("FEATURE IMPORTANCE")
print(f"{'='*50}")

importances = best_dt.feature_importances_
for name, imp in zip(iris.feature_names, importances):
    bar = "█" * int(imp * 40)
    print(f"  {name:20s}: {imp:.4f} {bar}")

plt.figure(figsize=(8, 4))
plt.barh(iris.feature_names, importances, color="steelblue", edgecolor="black")
plt.xlabel("Feature Importance")
plt.title("Decision Tree - Feature Importance (Iris)")
plt.tight_layout()
plt.show()


# ============================================================
# 6. Decision Tree Regression
# ============================================================
print(f"\n{'='*50}")
print("DECISION TREE REGRESSION")
print(f"{'='*50}")

np.random.seed(42)
X_reg = np.sort(5 * np.random.rand(80, 1), axis=0)
y_reg = np.sin(X_reg).ravel() + np.random.normal(0, 0.1, 80)

X_tr, X_te, y_tr, y_te = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

# Fit regression trees with different depths
plt.figure(figsize=(12, 4))
x_plot = np.linspace(0, 5, 500).reshape(-1, 1)

for i, depth in enumerate([2, 5, 20]):
    dtr = DecisionTreeRegressor(max_depth=depth, random_state=42)
    dtr.fit(X_tr, y_tr)
    y_plot = dtr.predict(x_plot)
    r2 = dtr.score(X_te, y_te)

    plt.subplot(1, 3, i + 1)
    plt.scatter(X_tr, y_tr, color="steelblue", s=20, alpha=0.6, label="Train")
    plt.scatter(X_te, y_te, color="orange", s=30, label="Test")
    plt.plot(x_plot, y_plot, "r-", linewidth=2, label=f"Tree (depth={depth})")
    plt.title(f"Depth={depth}, Test R²={r2:.3f}")
    plt.legend(fontsize=8)
    plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("Depth=2:  Underfitting (too simple)")
print("Depth=5:  Good fit")
print("Depth=20: Overfitting (too complex)")

print("\n--- Decision Tree complete! ---")
