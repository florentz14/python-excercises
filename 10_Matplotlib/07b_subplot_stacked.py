# -------------------------------------------------
# File Name: 07b_subplot_stacked.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Stacked subplots (2 rows, 1 col).
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)  # 100 points from 0 to 2*pi for smooth trigonometric curves

# =========================================================================
# Stacked subplots (2 rows, 1 column)
# =========================================================================

plt.figure(figsize=(7, 6))

plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x), "b-", linewidth=2)
plt.title("sin(x)")
plt.grid(True, alpha=0.3)

plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x), "r-", linewidth=2)
plt.title("cos(x)")
plt.grid(True, alpha=0.3)

plt.suptitle("Stacked Subplots (2 rows, 1 col)", fontsize=14)
plt.tight_layout()
plt.show()
