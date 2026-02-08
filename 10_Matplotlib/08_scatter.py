"""
Matplotlib - 08: Scatter Plots
===============================
Description: Create scatter plots to show the relationship between
             two variables. Customize colors, sizes, transparency,
             and add color maps.
"""

import matplotlib.pyplot as plt
import numpy as np

# =========================================================================
# Basic scatter plot
# =========================================================================

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

plt.figure(figsize=(6, 4))
plt.scatter(x, y)
plt.title("Basic Scatter Plot")
plt.xlabel("Age")
plt.ylabel("Speed")
plt.show()

# =========================================================================
# Compare two datasets
# =========================================================================

# Dataset 1
x1 = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y1 = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78]

# Dataset 2
x2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
y2 = [105, 95, 90, 85, 80, 75, 70, 65, 60, 55]

plt.figure(figsize=(7, 5))
plt.scatter(x1, y1, color="red", label="Morning", marker="o", s=80)
plt.scatter(x2, y2, color="blue", label="Afternoon", marker="s", s=80)
plt.title("Two Datasets Comparison")
plt.xlabel("Age")
plt.ylabel("Speed")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# =========================================================================
# Custom colors for each point
# =========================================================================

np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)   # Values 0-1 mapped to colormap
sizes = np.random.rand(50) * 500  # Random sizes

plt.figure(figsize=(7, 5))
scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6,
                      cmap="viridis", edgecolors="black", linewidth=0.5)
plt.colorbar(scatter, label="Color Value")
plt.title("Scatter with Colormap and Varying Sizes")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# =========================================================================
# Different colormaps
# =========================================================================

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Different Colormaps", fontsize=14)

cmaps = ["viridis", "plasma", "coolwarm", "RdYlGn"]
for ax, cmap in zip(axes.flat, cmaps):
    sc = ax.scatter(x, y, c=colors, s=100, cmap=cmap, edgecolors="gray")
    ax.set_title(f"cmap='{cmap}'")
    plt.colorbar(sc, ax=ax)

plt.tight_layout()
plt.show()

# =========================================================================
# Scatter with transparency (alpha)
# =========================================================================

x_large = np.random.randn(500)
y_large = np.random.randn(500)

plt.figure(figsize=(7, 5))
plt.scatter(x_large, y_large, alpha=0.3, color="steelblue", s=40)
plt.title("Scatter with Alpha (500 points)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True, alpha=0.3)
plt.show()

# =========================================================================
# Practical example: Student grades
# =========================================================================

hours_studied = [1, 2, 3, 3.5, 4, 5, 5.5, 6, 7, 8, 8.5, 9, 10]
exam_score = [30, 45, 50, 55, 60, 65, 70, 72, 80, 85, 88, 92, 95]

plt.figure(figsize=(7, 5))
plt.scatter(hours_studied, exam_score, color="coral", s=100,
            edgecolors="black", linewidth=0.8, zorder=5)

# Add trend line
z = np.polyfit(hours_studied, exam_score, 1)
p = np.poly1d(z)
x_line = np.linspace(0, 11, 100)
plt.plot(x_line, p(x_line), "b--", alpha=0.7, label="Trend line")

plt.title("Study Hours vs Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
