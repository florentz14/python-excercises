"""
Linear Regression - Predicting Continuous Values
==================================================
Supervised algorithm for predicting continuous numeric values.
Examples: house price, salary, sales.

Author: Florentino Báez
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Example dataset
X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("Predictions:", predictions)
print("MSE:", mean_squared_error(y_test, predictions))
