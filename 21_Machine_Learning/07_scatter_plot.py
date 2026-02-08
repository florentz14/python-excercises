"""
Machine Learning - Scatter Plot
=================================
Scatter plots display data points on a 2D plane (x, y).
They help visualize relationships between two variables:
- Positive correlation: as X increases, Y increases
- Negative correlation: as X increases, Y decreases
- No correlation: no clear pattern

Scatter plots are essential for understanding data before
building ML models.
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. Basic Scatter Plot
# ============================================================
# Hours studied vs Exam score
hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
scores = [35, 45, 50, 55, 65, 70, 72, 82, 88, 95]

plt.figure(figsize=(8, 5))
plt.scatter(hours, scores, color="steelblue", s=80, edgecolors="black")
plt.title("Hours Studied vs Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("Basic scatter plot: Shows positive correlation")
print("More hours studied -> higher exam scores")


# ============================================================
# 2. Random Scatter Plot - Looking for patterns
# ============================================================
np.random.seed(42)

# Positive correlation
x1 = np.random.normal(5, 1, 100)
y1 = x1 * 2 + np.random.normal(0, 1, 100)

# Negative correlation
x2 = np.random.normal(5, 1, 100)
y2 = -x2 * 1.5 + 20 + np.random.normal(0, 1, 100)

# No correlation
x3 = np.random.normal(5, 1, 100)
y3 = np.random.normal(10, 2, 100)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].scatter(x1, y1, c="steelblue", alpha=0.6, edgecolors="black", linewidth=0.5)
axes[0].set_title("Positive Correlation")
axes[0].set_xlabel("X")
axes[0].set_ylabel("Y")

axes[1].scatter(x2, y2, c="coral", alpha=0.6, edgecolors="black", linewidth=0.5)
axes[1].set_title("Negative Correlation")
axes[1].set_xlabel("X")

axes[2].scatter(x3, y3, c="mediumseagreen", alpha=0.6, edgecolors="black", linewidth=0.5)
axes[2].set_title("No Correlation")
axes[2].set_xlabel("X")

plt.tight_layout()
plt.show()

print("\nThree types of correlation visualized")


# ============================================================
# 3. Scatter Plot with Trend Line
# ============================================================
print(f"\n{'='*50}")
print("SCATTER PLOT WITH TREND LINE")
print(f"{'='*50}")

x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

# Fit a linear trend line
slope, intercept = np.polyfit(x, y, 1)
trend_line = slope * x + intercept

print(f"Slope: {slope:.2f}")
print(f"Intercept: {intercept:.2f}")
print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")

plt.figure(figsize=(8, 5))
plt.scatter(x, y, color="steelblue", s=80, edgecolors="black", zorder=5, label="Data")
plt.plot(sorted(x), [slope * xi + intercept for xi in sorted(x)],
         "r--", linewidth=2, label=f"Trend: y={slope:.1f}x+{intercept:.1f}")
plt.title("Scatter Plot with Trend Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ============================================================
# 4. Correlation Coefficient
# ============================================================
print(f"\n{'='*50}")
print("CORRELATION COEFFICIENT (r)")
print(f"{'='*50}")

# Pearson correlation coefficient (r)
# r = 1  -> perfect positive correlation
# r = -1 -> perfect negative correlation
# r = 0  -> no correlation

from scipy.stats import pearsonr

datasets = {
    "Positive":     (x1, y1),
    "Negative":     (x2, y2),
    "No correlation": (x3, y3),
}

for name, (xi, yi) in datasets.items():
    r, p_value = pearsonr(xi, yi)
    print(f"  {name:20s} -> r = {r:+.4f}, p-value = {p_value:.6f}")


# ============================================================
# 5. Scatter Plot with Color Map and Size
# ============================================================
print(f"\n{'='*50}")
print("SCATTER PLOT WITH COLOR MAP AND SIZE")
print(f"{'='*50}")

np.random.seed(42)
n = 50
x = np.random.rand(n) * 100          # x position
y = np.random.rand(n) * 100          # y position
colors = np.random.rand(n) * 100     # color intensity
sizes = np.random.rand(n) * 500 + 50 # point size

plt.figure(figsize=(8, 6))
scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6,
                      cmap="viridis", edgecolors="black", linewidth=0.5)
plt.colorbar(scatter, label="Intensity")
plt.title("Bubble Chart (Scatter with Size & Color)")
plt.xlabel("X")
plt.ylabel("Y")
plt.tight_layout()
plt.show()


# ============================================================
# 6. Real-world example: Age vs Blood Pressure
# ============================================================
print(f"\n{'='*50}")
print("REAL-WORLD: Age vs Blood Pressure")
print(f"{'='*50}")

np.random.seed(42)
age = np.random.randint(20, 80, 50)
blood_pressure = 90 + age * 0.5 + np.random.normal(0, 8, 50)

r, p = pearsonr(age, blood_pressure)
print(f"Correlation (r): {r:.4f}")
print(f"p-value:         {p:.6f}")
print(f"Interpretation: {'Significant' if p < 0.05 else 'Not significant'} correlation")

plt.figure(figsize=(8, 5))
plt.scatter(age, blood_pressure, c=age, cmap="Reds", s=60,
            edgecolors="black", linewidth=0.5, alpha=0.8)
plt.colorbar(label="Age")

# Trend line
z = np.polyfit(age, blood_pressure, 1)
p_line = np.poly1d(z)
x_line = np.linspace(20, 80, 100)
plt.plot(x_line, p_line(x_line), "b--", linewidth=2, label=f"Trend (r={r:.2f})")

plt.title("Age vs Blood Pressure")
plt.xlabel("Age (years)")
plt.ylabel("Systolic Blood Pressure (mmHg)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\n--- Scatter Plot complete! ---")
