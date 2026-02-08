# -------------------------------------------------
# File Name: 07d_subplot_mixed_layout.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Mixed layout: big left + two stacked right.
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)  # 100 points from 0 to 2*pi for smooth trigonometric curves

# =========================================================================
# Subplots with different sizes using GridSpec
# =========================================================================

fig = plt.figure(figsize=(10, 6))  # Start with an empty figure; we'll manually add subplots

# Big plot on the left
ax1 = fig.add_subplot(1, 2, 1)  # add_subplot() lets us place a subplot on part of the grid
ax1.plot(x, np.sin(x), "b-", linewidth=2)
ax1.set_title("Main Plot (Large)")
ax1.grid(True, alpha=0.3)

# Two small plots stacked on the right
ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(x, np.cos(x), "r-")
ax2.set_title("Top Right")
ax2.grid(True, alpha=0.3)

ax3 = fig.add_subplot(2, 2, 4)
ax3.plot(x, np.sin(x) * np.cos(x), "g-")
ax3.set_title("Bottom Right")
ax3.grid(True, alpha=0.3)

plt.suptitle("Mixed Layout", fontsize=14)
plt.tight_layout()
plt.show()
