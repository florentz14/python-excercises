# -------------------------------------------------
# File Name: 07a_subplot_side_by_side.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Two subplots side by side (1 row, 2 cols).
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)  # 100 points from 0 to 2*pi for smooth trigonometric curves

# =========================================================================
# Basic: Two subplots side by side (1 row, 2 columns)
# =========================================================================

plt.figure(figsize=(10, 4))

# subplot(rows, cols, index) — index counts left-to-right, top-to-bottom
plt.subplot(1, 2, 1)
plt.plot(x, np.sin(x), "b-")
plt.title("sin(x)")
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(x, np.cos(x), "r-")
plt.title("cos(x)")
plt.grid(True, alpha=0.3)

# suptitle() sets a title for the entire figure, not just one subplot
plt.suptitle("Two Subplots (1 row, 2 cols)", fontsize=14)
plt.tight_layout()
plt.show()
