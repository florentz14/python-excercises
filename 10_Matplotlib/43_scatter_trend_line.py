# -------------------------------------------------
# File Name: 08f_scatter_trend_line.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Student grades scatter with polyfit trend line.
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# =========================================================================
# Practical example: Student grades
# =========================================================================

hours_studied = [1, 2, 3, 3.5, 4, 5, 5.5, 6, 7, 8, 8.5, 9, 10]
exam_score = [30, 45, 50, 55, 60, 65, 70, 72, 80, 85, 88, 92, 95]

plt.figure(figsize=(7, 5))
plt.scatter(hours_studied, exam_score, color="coral", s=100,
            edgecolors="black", linewidth=0.8, zorder=5)  # zorder controls drawing order; higher values are drawn on top

# Add trend line
z = np.polyfit(hours_studied, exam_score, 1)  # polyfit degree=1 fits a straight line (linear regression)
p = np.poly1d(z)  # poly1d creates a callable polynomial from the fitted coefficients
x_line = np.linspace(0, 11, 100)
plt.plot(x_line, p(x_line), "b--", alpha=0.7, label="Trend line")

plt.title("Study Hours vs Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
