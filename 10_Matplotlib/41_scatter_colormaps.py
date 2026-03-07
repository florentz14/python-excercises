# -------------------------------------------------
# File Name: 08d_scatter_colormaps.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Different colormaps comparison (2x2 grid).
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# =========================================================================
# Different colormaps
# =========================================================================

# Reuse same data pattern as colormap example (x, y, colors)
np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Different Colormaps", fontsize=14)

cmaps = ["viridis", "plasma", "coolwarm", "RdYlGn"]
for ax, cmap in zip(axes.flat, cmaps):
    sc = ax.scatter(x, y, c=colors, s=100, cmap=cmap, edgecolors="gray")
    ax.set_title(f"cmap='{cmap}'")
    plt.colorbar(sc, ax=ax)

plt.tight_layout()
plt.show()
