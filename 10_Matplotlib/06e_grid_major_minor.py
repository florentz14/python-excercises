# -------------------------------------------------
# File Name: 06e_grid_major_minor.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Major and minor grid lines.
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# =========================================================================
# Major and minor grid lines
# =========================================================================

fig, ax = plt.subplots(figsize=(7, 5))

t = np.linspace(0, 2 * np.pi, 100)
ax.plot(t, np.sin(t), "b-", linewidth=2)

# Enable minor ticks
ax.minorticks_on()  # Enable minor tick marks between the major ticks

# Major grid (thicker, darker)
# "which" selects major, minor, or both grid levels
ax.grid(which="major", color="gray", linestyle="-", linewidth=0.8, alpha=0.7)

# Minor grid (thinner, lighter)
ax.grid(which="minor", color="gray", linestyle=":", linewidth=0.4, alpha=0.4)

ax.set_title("Major and Minor Grid Lines")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
plt.show()
