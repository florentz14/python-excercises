# -------------------------------------------------
# File Name: 06b_grid_axis.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Grid on specific axis: both, x-only, y-only (3 subplots).
# -------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 7, 4, 9, 1, 6, 3]

# =========================================================================
# Grid on specific axis
# =========================================================================

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

# Both axes (default)
axes[0].plot(x, y, "b-o")
axes[0].grid(True, axis="both")  # axis="both" draws grid lines for X and Y (this is the default)
axes[0].set_title("axis='both' (default)")

# X-axis only
axes[1].plot(x, y, "r-s")
axes[1].grid(True, axis="x")
axes[1].set_title("axis='x'")

# Y-axis only
axes[2].plot(x, y, "g-^")
axes[2].grid(True, axis="y")
axes[2].set_title("axis='y'")

plt.tight_layout()
plt.show()
