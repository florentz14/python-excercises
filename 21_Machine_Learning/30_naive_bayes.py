"""
Naive Bayes - Probabilistic Classification
===========================================
Based on Bayes' theorem.
Used in: spam detection, sentiment analysis, text classification.

Author: Florentino Báez
"""

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Example dataset
X = [[1, 20], [2, 21], [3, 22], [8, 30], [9, 31], [10, 32]]
y = [0, 0, 0, 1, 1, 1]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = GaussianNB()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Accuracy:", accuracy_score(y_test, predictions))
