"""
K-Nearest Neighbors (KNN) - Classification by Neighbors
========================================================
Classifies based on the K nearest neighbors.
If the 3 nearest neighbors are "red", this point is probably "red" too.

Author: Florentino Báez
"""

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Example dataset
X = [[1], [2], [3], [6], [7], [8]]
y = [0, 0, 0, 1, 1, 1]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Accuracy:", accuracy_score(y_test, predictions))
