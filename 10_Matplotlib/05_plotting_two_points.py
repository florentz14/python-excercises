# -------------------------------------------------
# File Name: 02a_plotting_two_points.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Line between two points.
# -------------------------------------------------

import matplotlib.pyplot as plt

# =========================================================================
# Basic plotting with two points
# =========================================================================

# plot() draws a line from point to point
# Point 1: (1, 3), Point 2: (8, 10)
plt.figure(figsize=(6, 4))  # Create figure canvas; figsize sets width x height in inches
plt.plot([1, 8], [3, 10])
plt.title("Line Between Two Points")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
