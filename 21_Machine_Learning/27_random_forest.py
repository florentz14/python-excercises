# -------------------------------------------------
# File Name: 27_random_forest.py
# Author: Florentino Báez
# Date: 21_Machine_Learning
# Description: Random forest ensemble of decision trees.
# -------------------------------------------------

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Dataset: [age, income] -> purchase (0/1)
X = [[20, 2000], [25, 2500], [30, 4000], [35, 5000], [40, 6000], [45, 7000]]
y = [0, 0, 1, 1, 1, 1]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Accuracy:", accuracy_score(y_test, predictions))
