# -------------------------------------------------
# File Name: 02d_plotting_keyword_args.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Plot with keyword arguments (color, linewidth, marker, etc.).
# -------------------------------------------------

import matplotlib.pyplot as plt

# =========================================================================
# Plotting with keyword arguments (more control)
# =========================================================================

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure(figsize=(6, 4))
# Using keyword arguments gives finer control over appearance
plt.plot(x, y,
         color="purple",
         linewidth=2.5,
         linestyle="--",
         marker="D",
         markersize=8,
         markerfacecolor="yellow",
         markeredgecolor="purple",
         label="Prime numbers")
plt.title("Plot with Keyword Arguments")
plt.legend()
plt.grid(True, alpha=0.3)  # alpha controls transparency (0=invisible, 1=opaque)
plt.show()
