"""
Gradient Boosting - Sequential Ensemble Learning
=================================================
Builds weak models sequentially, each correcting the errors of the previous one.
Excellent for tabular data and high-accuracy predictions.

Author: Florentino Baez
"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

# Example dataset
X = [[20, 2000], [25, 2500], [30, 4000], [35, 5000], [40, 6000], [45, 7000]]
y = [0, 0, 1, 1, 1, 1]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = GradientBoostingClassifier(random_state=42)

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Accuracy:", accuracy_score(y_test, predictions))
