# -------------------------------------------------
# File Name: 07e_subplot_shared_axes.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Shared Y-axis between subplots.
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)  # 100 points from 0 to 2*pi for smooth trigonometric curves

# =========================================================================
# Sharing axes between subplots
# =========================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4), sharey=True)  # sharey=True links the Y-axis scale so both subplots use the same range

ax1.plot(x, np.sin(x), "b-")
ax1.set_title("sin(x)")
ax1.set_ylabel("y")
ax1.grid(True, alpha=0.3)

ax2.plot(x, np.cos(x), "r-")
ax2.set_title("cos(x)")
ax2.grid(True, alpha=0.3)
# Note: Y-axis is shared, so labels appear only on the left

plt.suptitle("Shared Y-Axis", fontsize=14)
plt.tight_layout()
plt.show()

print("\n--- Subplot Summary ---")
print("plt.subplot(rows, cols, index)  -> Select subplot position")
print("fig, axes = plt.subplots(r, c)  -> Create grid of axes")
print("plt.suptitle('Title')           -> Title for entire figure")
print("plt.tight_layout()              -> Auto-adjust spacing")
print("sharey=True / sharex=True       -> Share axis between subplots")
