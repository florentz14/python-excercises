# -------------------------------------------------
# File Name: 26_decision_tree.py
# Author: Florentino Báez
# Date: 21_Machine_Learning
# Description: Decision tree for tree-structured classification.
# -------------------------------------------------

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Dataset: [age, income] → purchase (0/1)
X = [[20, 2000], [25, 2500], [30, 4000], [35, 5000], [40, 6000]]
y = [0, 0, 1, 1, 1]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Accuracy:", accuracy_score(y_test, predictions))
