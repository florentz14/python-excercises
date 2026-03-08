# -------------------------------------------------
# File Name: 24_linear_regression.py
# Author: Florentino Báez
# Date: 21_Machine_Learning
# Description: Linear regression for predicting continuous values.
# -------------------------------------------------

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
