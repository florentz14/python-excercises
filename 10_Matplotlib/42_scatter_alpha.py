# -------------------------------------------------
# File Name: 08e_scatter_alpha.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Scatter with transparency (500 points, randn).
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# =========================================================================
# Scatter with transparency (alpha)
# =========================================================================

x_large = np.random.randn(500)  # randn() draws from a standard normal distribution (mean=0, std=1)
y_large = np.random.randn(500)

plt.figure(figsize=(7, 5))
plt.scatter(x_large, y_large, alpha=0.3, color="steelblue", s=40)
plt.title("Scatter with Alpha (500 points)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True, alpha=0.3)
plt.show()
