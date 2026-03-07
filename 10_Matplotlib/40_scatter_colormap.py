# -------------------------------------------------
# File Name: 08c_scatter_colormap.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Scatter with Colormap — custom colors,
#              sizes, and viridis colormap.
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)  # Fix random seed for reproducible results
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)   # Random values 0-1; mapped to a colormap gradient
sizes = np.random.rand(50) * 500  # Random sizes (area in points^2); larger value = bigger dot

plt.figure(figsize=(7, 5))
# c= maps values to colors via cmap; s= sets individual dot sizes
scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6,
                      cmap="viridis", edgecolors="black", linewidth=0.5)
plt.colorbar(scatter, label="Color Value")  # Add a color scale bar showing how values map to colors
plt.title("Scatter with Colormap and Varying Sizes")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
