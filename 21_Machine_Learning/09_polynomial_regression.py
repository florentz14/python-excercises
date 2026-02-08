"""
Machine Learning - Polynomial Regression
==========================================
Polynomial Regression fits a curved line to data when the relationship
between X and Y is not linear.

Equation: y = b₀ + b₁x + b₂x² + b₃x³ + ... + bₙxⁿ

When to use:
- When a straight line doesn't fit the data well
- When scatter plot shows a curved pattern
- Common in real-world data (diminishing returns, growth curves)

Caution: High-degree polynomials can OVERFIT the data!
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# ============================================================
# 1. Why Linear Regression Fails (Curved Data)
# ============================================================
# Car passing toll booth: time of day vs number of cars
x = np.array([1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22])
y = np.array([100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100])

# Try linear regression
from scipy.stats import linregress
slope, intercept, r_val, _, _ = linregress(x, y)
y_linear = slope * x + intercept

print("Cars at toll booth throughout the day")
print(f"Linear R²: {r_val**2:.4f} (poor fit for curved data)")


# ============================================================
# 2. Polynomial Regression with numpy
# ============================================================
print(f"\n{'='*50}")
print("POLYNOMIAL REGRESSION (numpy)")
print(f"{'='*50}")

# Fit a polynomial of degree 3
coefficients = np.polyfit(x, y, 3)
poly_model = np.poly1d(coefficients)

print(f"Polynomial equation (degree 3):")
print(f"  {poly_model}")

# Predict using the polynomial model
x_smooth = np.linspace(1, 22, 100)
y_poly = poly_model(x_smooth)

# R² for polynomial
y_pred_poly = poly_model(x)
r2_poly = r2_score(y, y_pred_poly)
print(f"Polynomial R²: {r2_poly:.4f}")

# Visualization
plt.figure(figsize=(10, 5))
plt.scatter(x, y, color="steelblue", s=80, edgecolors="black", zorder=5, label="Data")
plt.plot(x, y_linear, "g--", linewidth=2, label=f"Linear (R²={r_val**2:.3f})")
plt.plot(x_smooth, y_poly, "r-", linewidth=2, label=f"Polynomial deg 3 (R²={r2_poly:.3f})")
plt.title("Linear vs Polynomial Regression")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Cars")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ============================================================
# 3. Polynomial Regression with sklearn
# ============================================================
print(f"\n{'='*50}")
print("POLYNOMIAL REGRESSION (sklearn)")
print(f"{'='*50}")

X = x.reshape(-1, 1)

# Transform features to polynomial features
poly_features = PolynomialFeatures(degree=3)
X_poly = poly_features.fit_transform(X)

print(f"Original features shape: {X.shape}")
print(f"Polynomial features shape: {X_poly.shape}")
print(f"Feature names: {poly_features.get_feature_names_out()}")

# Fit linear regression on polynomial features
model = LinearRegression()
model.fit(X_poly, y)

y_pred_sklearn = model.predict(X_poly)
r2_sklearn = r2_score(y, y_pred_sklearn)
print(f"R² score: {r2_sklearn:.4f}")


# ============================================================
# 4. Prediction with Polynomial Model
# ============================================================
print(f"\n{'='*50}")
print("PREDICTION")
print(f"{'='*50}")

# Predict number of cars at hour 17 (5 PM)
hour = 17
predicted = poly_model(hour)
print(f"Predicted cars at hour {hour}: {predicted:.0f}")

# Predict for multiple hours
hours = [6, 10, 14, 17, 20, 23]
for h in hours:
    pred = poly_model(h)
    print(f"  Hour {h:2d}:00 -> {pred:.0f} cars")


# ============================================================
# 5. Comparing Different Polynomial Degrees
# ============================================================
print(f"\n{'='*50}")
print("COMPARING POLYNOMIAL DEGREES")
print(f"{'='*50}")

plt.figure(figsize=(12, 5))
plt.scatter(x, y, color="black", s=60, zorder=5, label="Data")

colors = ["green", "blue", "red", "purple", "orange"]
for degree, color in zip([1, 2, 3, 4, 6], colors):
    coeffs = np.polyfit(x, y, degree)
    model_p = np.poly1d(coeffs)
    y_pred_d = model_p(x)
    r2_d = r2_score(y, y_pred_d)
    plt.plot(x_smooth, model_p(x_smooth), color=color, linewidth=2,
             label=f"Degree {degree} (R²={r2_d:.4f})")
    print(f"  Degree {degree}: R² = {r2_d:.4f}")

plt.title("Polynomial Regression - Different Degrees")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Cars")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ============================================================
# 6. Overfitting Warning
# ============================================================
print(f"\n{'='*50}")
print("OVERFITTING DEMONSTRATION")
print(f"{'='*50}")

np.random.seed(42)
x_train = np.sort(np.random.uniform(0, 10, 15))
y_train = np.sin(x_train) + np.random.normal(0, 0.3, 15)

# Test data
x_test = np.sort(np.random.uniform(0, 10, 10))
y_test = np.sin(x_test) + np.random.normal(0, 0.3, 10)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
x_plot = np.linspace(0, 10, 200)

for ax, degree, title in zip(axes, [1, 3, 15],
                              ["Underfitting (deg=1)", "Good Fit (deg=3)", "Overfitting (deg=15)"]):
    coeffs = np.polyfit(x_train, y_train, degree)
    model_p = np.poly1d(coeffs)

    r2_train = r2_score(y_train, model_p(x_train))
    r2_test = r2_score(y_test, np.clip(model_p(x_test), -10, 10))

    ax.scatter(x_train, y_train, color="steelblue", s=40, label="Train")
    ax.scatter(x_test, y_test, color="orange", s=40, marker="^", label="Test")
    y_plot = np.clip(model_p(x_plot), -3, 3)
    ax.plot(x_plot, y_plot, "r-", linewidth=2)
    ax.set_title(f"{title}\nTrain R²={r2_train:.3f}")
    ax.set_ylim(-3, 3)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("Underfitting: Model is too simple (high bias)")
print("Overfitting:  Model is too complex (high variance)")
print("Good fit:     Right balance between bias and variance")

print("\n--- Polynomial Regression complete! ---")
