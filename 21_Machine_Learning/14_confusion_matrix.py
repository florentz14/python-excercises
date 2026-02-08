"""
Machine Learning - Confusion Matrix
======================================
A confusion matrix summarizes classification model performance by showing
the counts of correct and incorrect predictions for each class.

For binary classification:
                    Predicted
                  Pos    Neg
Actual  Pos  [  TP  |  FN  ]
        Neg  [  FP  |  TN  ]

TP = True Positive  (correctly predicted positive)
TN = True Negative  (correctly predicted negative)
FP = False Positive (predicted positive, but actually negative) — Type I error
FN = False Negative (predicted negative, but actually positive) — Type II error

Key Metrics:
- Accuracy  = (TP + TN) / Total
- Precision = TP / (TP + FP)   — "Of predicted positives, how many are correct?"
- Recall    = TP / (TP + FN)   — "Of actual positives, how many did we find?"
- F1 Score  = 2 * (Precision * Recall) / (Precision + Recall)
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import (confusion_matrix, classification_report,
                             accuracy_score, precision_score, recall_score,
                             f1_score, ConfusionMatrixDisplay)

# ============================================================
# 1. Basic Confusion Matrix
# ============================================================
print("BASIC CONFUSION MATRIX")
print("=" * 50)

# Simulated predictions
y_actual    = [1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
y_predicted = [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1]

cm = confusion_matrix(y_actual, y_predicted)
print(f"Confusion Matrix:\n{cm}")
print(f"""
Layout:
  TN={cm[0][0]}  FP={cm[0][1]}
  FN={cm[1][0]}  TP={cm[1][1]}
""")

# Extract values
tn, fp, fn, tp = cm.ravel()
print(f"True Positives:  {tp}")
print(f"True Negatives:  {tn}")
print(f"False Positives: {fp} (Type I error)")
print(f"False Negatives: {fn} (Type II error)")


# ============================================================
# 2. Metrics Calculated from Confusion Matrix
# ============================================================
print(f"\n{'='*50}")
print("METRICS FROM CONFUSION MATRIX")
print(f"{'='*50}")

accuracy = accuracy_score(y_actual, y_predicted)
precision = precision_score(y_actual, y_predicted)
recall = recall_score(y_actual, y_predicted)
f1 = f1_score(y_actual, y_predicted)

print(f"Accuracy:  {accuracy:.4f}  (correct / total)")
print(f"Precision: {precision:.4f}  (TP / (TP+FP))")
print(f"Recall:    {recall:.4f}  (TP / (TP+FN))")
print(f"F1 Score:  {f1:.4f}  (harmonic mean of precision & recall)")

# Manual calculation
print(f"\nManual verification:")
print(f"  Accuracy  = ({tp}+{tn}) / ({tp}+{tn}+{fp}+{fn}) = {(tp+tn)/(tp+tn+fp+fn):.4f}")
print(f"  Precision = {tp} / ({tp}+{fp}) = {tp/(tp+fp):.4f}")
print(f"  Recall    = {tp} / ({tp}+{fn}) = {tp/(tp+fn):.4f}")


# ============================================================
# 3. Visualizing the Confusion Matrix
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Default display
ConfusionMatrixDisplay.from_predictions(
    y_actual, y_predicted, display_labels=["Negative", "Positive"],
    cmap="Blues", ax=axes[0]
)
axes[0].set_title("Confusion Matrix (Counts)")

# Normalized display
ConfusionMatrixDisplay.from_predictions(
    y_actual, y_predicted, display_labels=["Negative", "Positive"],
    normalize="true", cmap="Oranges", ax=axes[1], values_format=".2%"
)
axes[1].set_title("Confusion Matrix (Normalized)")

plt.tight_layout()
plt.show()


# ============================================================
# 4. Multi-class Confusion Matrix
# ============================================================
print(f"\n{'='*50}")
print("MULTI-CLASS CONFUSION MATRIX")
print(f"{'='*50}")

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42
)

dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train, y_train)
y_pred_iris = dt.predict(X_test)

cm_iris = confusion_matrix(y_test, y_pred_iris)
print(f"Confusion Matrix (3 classes):\n{cm_iris}")

print(f"\nClassification Report:")
print(classification_report(y_test, y_pred_iris, target_names=iris.target_names))

# Visualize
plt.figure(figsize=(7, 5))
ConfusionMatrixDisplay.from_predictions(
    y_test, y_pred_iris, display_labels=iris.target_names,
    cmap="YlGnBu"
)
plt.title("Iris Classification - Confusion Matrix")
plt.tight_layout()
plt.show()


# ============================================================
# 5. When Metrics Disagree
# ============================================================
print(f"{'='*50}")
print("PRECISION vs RECALL TRADE-OFF")
print(f"{'='*50}")

print("""
Scenario: Medical test for disease (positive = disease)

High Precision, Low Recall (conservative):
  - Very few false alarms, but misses many sick patients
  - Example: Only diagnose if VERY certain

High Recall, Low Precision (aggressive):
  - Catches almost all sick patients, but many false alarms
  - Example: Diagnose if even slight suspicion

Choose based on context:
  - Spam filter: High precision (don't lose real emails)
  - Cancer screening: High recall (don't miss any cases)
  - Balance: Use F1 Score
""")

# Simulate: medical screening
np.random.seed(42)
y_true = np.array([1]*20 + [0]*80)  # 20% have the disease
y_conservative = np.array([1]*10 + [0]*10 + [0]*80)  # Conservative model
y_aggressive   = np.array([1]*20 + [1]*30 + [0]*50)  # Aggressive model

for name, y_p in [("Conservative", y_conservative), ("Aggressive", y_aggressive)]:
    p = precision_score(y_true, y_p)
    r = recall_score(y_true, y_p)
    f = f1_score(y_true, y_p)
    print(f"  {name:15s} -> Precision: {p:.2f}, Recall: {r:.2f}, F1: {f:.2f}")


# ============================================================
# 6. Specificity and Sensitivity
# ============================================================
print(f"\n{'='*50}")
print("SPECIFICITY AND SENSITIVITY")
print(f"{'='*50}")

cm_example = confusion_matrix(y_actual, y_predicted)
tn, fp, fn, tp = cm_example.ravel()

sensitivity = tp / (tp + fn)  # Same as Recall
specificity = tn / (tn + fp)  # True Negative Rate

print(f"Sensitivity (Recall / TPR): {sensitivity:.4f}")
print(f"  -> How well does the model detect positives?")
print(f"Specificity (TNR):          {specificity:.4f}")
print(f"  -> How well does the model detect negatives?")

print("\n--- Confusion Matrix complete! ---")
