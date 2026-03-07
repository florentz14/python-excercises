# -------------------------------------------------
# File Name: 01a_pyplot_basic_plot.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Basic plot: Y-only vs X+Y (subplot with 2 panels).
# -------------------------------------------------

import matplotlib.pyplot as plt

# =========================================================================
# Basic plot with plt.plot()
# =========================================================================

# If you provide a single list, it becomes the Y values (X = 0, 1, 2...)
plt.figure(figsize=(8, 4))  # Create a new figure; figsize=(width, height) in inches

plt.subplot(1, 2, 1)  # Select subplot: (rows, cols, index) — index starts at 1
plt.plot([10, 20, 15, 25, 30])
plt.title("Y values only (X = auto)")

# If you provide two lists, first is X, second is Y
plt.subplot(1, 2, 2)
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("X and Y values")

plt.tight_layout()  # Automatically adjust spacing to prevent overlapping
plt.show()  # Render and display the figure window
