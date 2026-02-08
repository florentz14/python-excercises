"""
Machine Learning - AUC-ROC Curve
==================================
The ROC (Receiver Operating Characteristic) curve evaluates
binary classification models at ALL possible thresholds.

Key concepts:
- TPR (True Positive Rate / Recall / Sensitivity) = TP / (TP + FN)
- FPR (False Positive Rate / 1-Specificity) = FP / (FP + TN)
- ROC Curve: plots TPR vs FPR at different thresholds
- AUC (Area Under the Curve): single number summary
  - AUC = 1.0: Perfect classifier
  - AUC = 0.5: Random classifier (no skill)
  - AUC < 0.5: Worse than random

Why use AUC-ROC?
- Works well with imbalanced datasets
- Threshold-independent evaluation
- Compares models regardless of classification threshold
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import (roc_curve, roc_auc_score, auc,
                             RocCurveDisplay, precision_recall_curve,
                             average_precision_score)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# ============================================================
# 1. Understanding the ROC Curve
# ============================================================
print("UNDERSTANDING THE ROC CURVE")
print("=" * 50)

# Create binary classification data
np.random.seed(42)
X, y = make_classification(n_samples=1000, n_features=10,
                            n_informative=5, n_redundant=2,
                            random_state=42)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train a logistic regression model
lr = LogisticRegression(max_iter=200)
lr.fit(X_train, y_train)

# Get predicted probabilities (not class labels)
y_proba = lr.predict_proba(X_test)[:, 1]  # Probability of class 1

# Calculate ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)

print(f"AUC Score: {roc_auc:.4f}")
print(f"\nSample thresholds and their TPR/FPR:")
print(f"{'Threshold':>10s} {'FPR':>8s} {'TPR':>8s}")
print("-" * 28)
for i in range(0, len(thresholds), len(thresholds) // 8):
    print(f"{thresholds[i]:>10.4f} {fpr[i]:>8.4f} {tpr[i]:>8.4f}")


# ============================================================
# 2. Plotting the ROC Curve
# ============================================================
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, "b-", linewidth=2, label=f"Logistic Regression (AUC = {roc_auc:.4f})")
plt.plot([0, 1], [0, 1], "r--", linewidth=1, label="Random Classifier (AUC = 0.5)")
plt.fill_between(fpr, tpr, alpha=0.1, color="blue")

plt.xlabel("False Positive Rate (FPR)")
plt.ylabel("True Positive Rate (TPR)")
plt.title("ROC Curve")
plt.legend(loc="lower right")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ============================================================
# 3. Comparing Multiple Models
# ============================================================
print(f"\n{'='*50}")
print("COMPARING MODELS WITH ROC-AUC")
print(f"{'='*50}")

models = {
    "Logistic Regression": LogisticRegression(max_iter=200),
    "Decision Tree":       DecisionTreeClassifier(max_depth=5, random_state=42),
    "Random Forest":       RandomForestClassifier(n_estimators=100, random_state=42),
}

plt.figure(figsize=(8, 6))

for name, model in models.items():
    model.fit(X_train, y_train)
    y_prob = model.predict_proba(X_test)[:, 1]
    fpr_m, tpr_m, _ = roc_curve(y_test, y_prob)
    auc_m = auc(fpr_m, tpr_m)
    plt.plot(fpr_m, tpr_m, linewidth=2, label=f"{name} (AUC = {auc_m:.4f})")
    print(f"  {name:25s}: AUC = {auc_m:.4f}")

plt.plot([0, 1], [0, 1], "k--", linewidth=1, label="Random (AUC = 0.5)")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curves - Model Comparison")
plt.legend(loc="lower right")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ============================================================
# 4. Effect of Threshold
# ============================================================
print(f"\n{'='*50}")
print("EFFECT OF THRESHOLD")
print(f"{'='*50}")

y_proba_lr = lr.predict_proba(X_test)[:, 1]

print(f"{'Threshold':>10s} {'Accuracy':>10s} {'Precision':>10s} {'Recall':>10s} {'F1':>10s}")
print("-" * 52)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

for threshold in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
    y_pred_t = (y_proba_lr >= threshold).astype(int)
    acc = accuracy_score(y_test, y_pred_t)
    prec = precision_score(y_test, y_pred_t, zero_division=0)
    rec = recall_score(y_test, y_pred_t)
    f1 = f1_score(y_test, y_pred_t, zero_division=0)
    print(f"{threshold:>10.1f} {acc:>10.4f} {prec:>10.4f} {rec:>10.4f} {f1:>10.4f}")


# ============================================================
# 5. Precision-Recall Curve (Alternative to ROC)
# ============================================================
print(f"\n{'='*50}")
print("PRECISION-RECALL CURVE")
print(f"{'='*50}")

# Better for imbalanced datasets
X_imb, y_imb = make_classification(n_samples=1000, n_features=10,
                                     weights=[0.9, 0.1],
                                     random_state=42)
X_tr_i, X_te_i, y_tr_i, y_te_i = train_test_split(X_imb, y_imb, test_size=0.3, random_state=42)

lr_imb = LogisticRegression(max_iter=200)
lr_imb.fit(X_tr_i, y_tr_i)
y_prob_imb = lr_imb.predict_proba(X_te_i)[:, 1]

# ROC AUC
roc_auc_imb = roc_auc_score(y_te_i, y_prob_imb)

# Precision-Recall
precision_curve, recall_curve, _ = precision_recall_curve(y_te_i, y_prob_imb)
avg_precision = average_precision_score(y_te_i, y_prob_imb)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# ROC
fpr_i, tpr_i, _ = roc_curve(y_te_i, y_prob_imb)
axes[0].plot(fpr_i, tpr_i, "b-", linewidth=2, label=f"AUC = {roc_auc_imb:.4f}")
axes[0].plot([0, 1], [0, 1], "r--")
axes[0].set_title("ROC Curve (Imbalanced Data)")
axes[0].set_xlabel("FPR")
axes[0].set_ylabel("TPR")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Precision-Recall
axes[1].plot(recall_curve, precision_curve, "g-", linewidth=2,
             label=f"Avg Precision = {avg_precision:.4f}")
axes[1].set_title("Precision-Recall Curve (Imbalanced)")
axes[1].set_xlabel("Recall")
axes[1].set_ylabel("Precision")
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"Imbalanced data (90%/10% split):")
print(f"  ROC AUC:           {roc_auc_imb:.4f}")
print(f"  Avg Precision (PR): {avg_precision:.4f}")
print("\nFor imbalanced data, PR curve is often more informative than ROC")


# ============================================================
# 6. Multi-class ROC-AUC
# ============================================================
print(f"\n{'='*50}")
print("MULTI-CLASS ROC-AUC")
print(f"{'='*50}")

from sklearn.datasets import load_iris
from sklearn.preprocessing import label_binarize

iris = load_iris()
X_tr_m, X_te_m, y_tr_m, y_te_m = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42
)

lr_multi = LogisticRegression(max_iter=200)
lr_multi.fit(X_tr_m, y_tr_m)

# One-vs-Rest AUC
y_prob_multi = lr_multi.predict_proba(X_te_m)
auc_ovr = roc_auc_score(y_te_m, y_prob_multi, multi_class="ovr")
auc_ovo = roc_auc_score(y_te_m, y_prob_multi, multi_class="ovo")

print(f"Multi-class AUC (One-vs-Rest): {auc_ovr:.4f}")
print(f"Multi-class AUC (One-vs-One):  {auc_ovo:.4f}")

print("\n--- AUC-ROC Curve complete! ---")
