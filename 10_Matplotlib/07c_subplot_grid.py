# -------------------------------------------------
# File Name: 07c_subplot_grid.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: 2x3 grid of subplots with trig functions.
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)  # 100 points from 0 to 2*pi for smooth trigonometric curves

# =========================================================================
# Grid of subplots (2 rows, 3 columns)
# =========================================================================

fig, axes = plt.subplots(2, 3, figsize=(14, 8))  # Returns a Figure and a 2x3 array of Axes objects
fig.suptitle("2x3 Grid of Subplots", fontsize=16)

functions = [
    (np.sin, "sin(x)", "blue"),
    (np.cos, "cos(x)", "red"),
    (np.tan, "tan(x)", "green"),
    (lambda x: np.sin(2*x), "sin(2x)", "purple"),
    (lambda x: np.cos(2*x), "cos(2x)", "orange"),
    (lambda x: np.sin(x)**2, "sin^2(x)", "brown")
]

for ax, (func, title, color) in zip(axes.flat, functions):
    y = func(x)
    if title == "tan(x)":
        y = np.clip(y, -5, 5)  # Clip extreme values of tan(x) to keep the plot readable
    ax.plot(x, y, color=color, linewidth=2)
    ax.set_title(title)
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
