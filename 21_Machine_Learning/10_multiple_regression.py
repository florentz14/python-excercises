"""
Machine Learning - Multiple Regression
========================================
Multiple Regression uses TWO OR MORE independent variables (features)
to predict a dependent variable (target).

Equation: y = b₀ + b₁x₁ + b₂x₂ + ... + bₙxₙ

Example: Predicting car CO2 emissions based on:
  - Engine volume (cm³)
  - Weight (kg)
  - Number of cylinders
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

# ============================================================
# 1. Creating a Sample Dataset
# ============================================================
np.random.seed(42)
n = 100

# Features
engine_volume = np.random.uniform(1.0, 5.0, n)          # liters
weight = np.random.uniform(1000, 2500, n)                # kg
horsepower = np.random.uniform(80, 350, n)               # hp

# Target: CO2 emissions (influenced by all features + noise)
co2 = (50 + 20 * engine_volume + 0.03 * weight + 0.1 * horsepower
       + np.random.normal(0, 10, n))

df = pd.DataFrame({
    "Engine_Volume": engine_volume.round(2),
    "Weight": weight.round(0),
    "Horsepower": horsepower.round(0),
    "CO2_Emissions": co2.round(1)
})

print("Sample Dataset (first 5 rows):")
print(df.head().to_string(index=False))
print(f"\nShape: {df.shape}")
print(f"\nStatistics:")
print(df.describe().round(2).to_string())


# ============================================================
# 2. Multiple Regression with sklearn
# ============================================================
print(f"\n{'='*50}")
print("MULTIPLE REGRESSION MODEL")
print(f"{'='*50}")

X = df[["Engine_Volume", "Weight", "Horsepower"]]
y = df["CO2_Emissions"]

model = LinearRegression()
model.fit(X, y)

print(f"Intercept (b₀):            {model.intercept_:.4f}")
print(f"Coefficient Engine Volume:  {model.coef_[0]:.4f}")
print(f"Coefficient Weight:         {model.coef_[1]:.4f}")
print(f"Coefficient Horsepower:     {model.coef_[2]:.4f}")
print(f"\nEquation:")
print(f"  CO2 = {model.intercept_:.2f} + {model.coef_[0]:.2f}×EngVol"
      f" + {model.coef_[1]:.4f}×Weight + {model.coef_[2]:.2f}×HP")


# ============================================================
# 3. Making Predictions
# ============================================================
print(f"\n{'='*50}")
print("PREDICTIONS")
print(f"{'='*50}")

# Predict CO2 for a car with: 2.5L engine, 1500kg, 150hp
new_car = np.array([[2.5, 1500, 150]])
predicted_co2 = model.predict(new_car)
print(f"Car: 2.5L engine, 1500kg, 150hp")
print(f"Predicted CO2: {predicted_co2[0]:.1f} g/km")

# Multiple predictions
cars = pd.DataFrame({
    "Engine_Volume": [1.2, 2.0, 3.0, 4.5],
    "Weight":        [1100, 1400, 1800, 2200],
    "Horsepower":    [90, 150, 220, 300]
})

predictions = model.predict(cars)
cars["Predicted_CO2"] = predictions.round(1)
print(f"\nMultiple predictions:")
print(cars.to_string(index=False))


# ============================================================
# 4. Model Evaluation
# ============================================================
print(f"\n{'='*50}")
print("MODEL EVALUATION")
print(f"{'='*50}")

y_pred = model.predict(X)
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

print(f"R² score:  {r2:.4f} ({r2*100:.1f}% of variance explained)")
print(f"RMSE:      {rmse:.4f}")

# Actual vs Predicted plot
plt.figure(figsize=(7, 5))
plt.scatter(y, y_pred, alpha=0.6, edgecolors="black", linewidth=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], "r--", linewidth=2, label="Perfect fit")
plt.xlabel("Actual CO2 Emissions")
plt.ylabel("Predicted CO2 Emissions")
plt.title(f"Actual vs Predicted (R² = {r2:.4f})")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ============================================================
# 5. Feature Importance (Coefficients)
# ============================================================
print(f"\n{'='*50}")
print("FEATURE IMPORTANCE")
print(f"{'='*50}")

feature_names = ["Engine Volume", "Weight", "Horsepower"]
coefficients = model.coef_

# Standardize to compare importance fairly
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
model_scaled = LinearRegression()
model_scaled.fit(X_scaled, y)

print("Standardized coefficients (comparable importance):")
for name, coef in zip(feature_names, model_scaled.coef_):
    bar = "█" * int(abs(coef))
    print(f"  {name:20s}: {coef:+8.4f} {bar}")

plt.figure(figsize=(8, 4))
colors = ["steelblue" if c > 0 else "coral" for c in model_scaled.coef_]
plt.barh(feature_names, model_scaled.coef_, color=colors, edgecolor="black")
plt.xlabel("Standardized Coefficient")
plt.title("Feature Importance")
plt.axvline(x=0, color="black", linewidth=0.5)
plt.tight_layout()
plt.show()


# ============================================================
# 6. Train/Test Split Evaluation
# ============================================================
print(f"\n{'='*50}")
print("TRAIN/TEST EVALUATION")
print(f"{'='*50}")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model2 = LinearRegression()
model2.fit(X_train, y_train)

train_r2 = model2.score(X_train, y_train)
test_r2 = model2.score(X_test, y_test)

print(f"Training R²: {train_r2:.4f}")
print(f"Testing R²:  {test_r2:.4f}")

if abs(train_r2 - test_r2) < 0.05:
    print("Model generalizes well (train ≈ test)")
elif train_r2 > test_r2:
    print("Possible overfitting (train >> test)")
else:
    print("Possible underfitting")

print("\n--- Multiple Regression complete! ---")
