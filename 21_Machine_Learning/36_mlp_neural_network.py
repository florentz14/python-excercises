"""
MLP Neural Network - Multi-Layer Perceptron
============================================
Basic neural network with hidden layers for capturing non-linear relationships.
Use when classical models are not sufficient for the problem complexity.

Author: Florentino Baez
"""

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Example dataset
X = [[1, 2], [2, 3], [3, 4], [8, 8], [9, 9], [10, 10]]
y = [0, 0, 0, 1, 1, 1]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model (2 hidden layers of 10 neurons each)
model = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000, random_state=42)

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Accuracy:", accuracy_score(y_test, predictions))
