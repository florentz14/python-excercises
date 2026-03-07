"""
XGBoost - Optimized Gradient Boosting
======================================
Highly optimized boosting implementation. Very popular in Kaggle and production.
Requires: pip install xgboost

Author: Florentino Baez
"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier

# Example dataset
X = [[20, 2000], [25, 2500], [30, 4000], [35, 5000], [40, 6000], [45, 7000]]
y = [0, 0, 1, 1, 1, 1]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model (eval_metric for compatibility with newer sklearn)
model = XGBClassifier(eval_metric="logloss")

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Accuracy:", accuracy_score(y_test, predictions))
