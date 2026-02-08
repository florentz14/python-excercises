"""
Machine Learning - Linear Regression
======================================
Linear Regression finds the relationship between a dependent variable (y)
and one independent variable (x) by fitting a straight line.

Equation: y = mx + b
Where:
  m = slope (how much y changes for each unit change in x)
  b = intercept (value of y when x = 0)

Uses: Predicting trends, understanding relationships between variables.

Key metrics:
- R² (R-squared): How well the line fits the data (0 to 1, closer to 1 is better)
- Slope: Direction and strength of the relationship
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# ============================================================
# 1. Simple Linear Regression with scipy
# ============================================================
# Car age vs speed
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

print("Linear Regression: Car Age vs Speed")
print(f"  Slope (m):     {slope:.4f}")
print(f"  Intercept (b): {intercept:.4f}")
print(f"  R-value:       {r_value:.4f}")
print(f"  R² value:      {r_value**2:.4f}")
print(f"  P-value:       {p_value:.4f}")
print(f"  Std error:     {std_err:.4f}")
print(f"  Equation:      y = {slope:.2f}x + {intercept:.2f}")


# ============================================================
# 2. Prediction
# ============================================================
print(f"\n{'='*50}")
print("PREDICTION")
print(f"{'='*50}")

# Predict speed for a 10-year-old car
age = 10
predicted_speed = slope * age + intercept
print(f"Predicted speed for a {age}-year-old car: {predicted_speed:.2f} km/h")

# Predict for multiple values
ages_to_predict = [1, 5, 10, 15, 20]
for a in ages_to_predict:
    pred = slope * a + intercept
    print(f"  Age {a:2d} years -> Speed: {pred:.1f} km/h")


# ============================================================
# 3. Visualizing the Regression Line
# ============================================================
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color="steelblue", s=80, edgecolors="black", zorder=5, label="Data")

# Plot regression line
x_line = np.linspace(0, 20, 100)
y_line = slope * x_line + intercept
plt.plot(x_line, y_line, "r-", linewidth=2, label=f"y = {slope:.2f}x + {intercept:.2f}")

plt.title(f"Linear Regression (R² = {r_value**2:.4f})")
plt.xlabel("Car Age (years)")
plt.ylabel("Speed (km/h)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ============================================================
# 4. R-squared explained
# ============================================================
print(f"\n{'='*50}")
print("R-SQUARED EXPLAINED")
print(f"{'='*50}")

print(f"""
R² = {r_value**2:.4f}

R² measures how well the regression line fits the data:
  R² = 1.0 -> Perfect fit (all points on the line)
  R² = 0.0 -> No relationship (line doesn't explain anything)

Our R² = {r_value**2:.4f} means the car's age explains
approximately {r_value**2*100:.1f}% of the variation in speed.
""")


# ============================================================
# 5. Linear Regression with sklearn
# ============================================================
print(f"{'='*50}")
print("LINEAR REGRESSION WITH SKLEARN")
print(f"{'='*50}")

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

X = x.reshape(-1, 1)  # sklearn expects 2D array for features

model = LinearRegression()
model.fit(X, y)

print(f"  Slope (coef):      {model.coef_[0]:.4f}")
print(f"  Intercept:         {model.intercept_:.4f}")

y_pred = model.predict(X)
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

print(f"  R² score:          {r2:.4f}")
print(f"  RMSE:              {rmse:.4f}")


# ============================================================
# 6. When Linear Regression fails (bad R²)
# ============================================================
print(f"\n{'='*50}")
print("GOOD vs BAD FIT")
print(f"{'='*50}")

np.random.seed(42)

# Good fit: strong linear relationship
x_good = np.arange(1, 21)
y_good = 3 * x_good + 5 + np.random.normal(0, 3, 20)

# Bad fit: no linear relationship (quadratic data)
x_bad = np.arange(1, 21)
y_bad = (x_bad - 10)**2 + np.random.normal(0, 5, 20)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Good fit plot
s1, i1, r1, _, _ = stats.linregress(x_good, y_good)
axes[0].scatter(x_good, y_good, color="steelblue", edgecolors="black")
axes[0].plot(x_good, s1 * x_good + i1, "r-", linewidth=2)
axes[0].set_title(f"Good Fit (R² = {r1**2:.4f})")
axes[0].set_xlabel("X")
axes[0].set_ylabel("Y")
axes[0].grid(True, alpha=0.3)

# Bad fit plot
s2, i2, r2_val, _, _ = stats.linregress(x_bad, y_bad)
axes[1].scatter(x_bad, y_bad, color="coral", edgecolors="black")
axes[1].plot(x_bad, s2 * x_bad + i2, "r-", linewidth=2)
axes[1].set_title(f"Bad Fit (R² = {r2_val**2:.4f})")
axes[1].set_xlabel("X")
axes[1].set_ylabel("Y")
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("When R² is low, a linear model is not appropriate.")
print("Consider polynomial or other non-linear models.")


# ============================================================
# 7. Residuals Analysis
# ============================================================
print(f"\n{'='*50}")
print("RESIDUALS ANALYSIS")
print(f"{'='*50}")

y_pred_good = s1 * x_good + i1
residuals = y_good - y_pred_good

print(f"Residuals (first 5): {residuals[:5].round(2)}")
print(f"Mean of residuals:   {np.mean(residuals):.4f} (should be ~0)")
print(f"Std of residuals:    {np.std(residuals):.4f}")

plt.figure(figsize=(8, 4))
plt.scatter(y_pred_good, residuals, color="steelblue", edgecolors="black")
plt.axhline(y=0, color="red", linestyle="--")
plt.title("Residuals Plot")
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("Good residual plot: randomly scattered around 0")
print("Bad residual plot: shows patterns (need a different model)")

print("\n--- Linear Regression complete! ---")
