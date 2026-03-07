# -------------------------------------------------
# File Name: 04a_line_styles.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Line styles comparison (2x2 grid: solid, dashed, dashdot, dotted).
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)

# =========================================================================
# Line styles
# =========================================================================

fig, axes = plt.subplots(2, 2, figsize=(10, 8))  # 2x2 grid of axes for comparing all four line styles
fig.suptitle("Line Styles", fontsize=14)

styles = [
    ("solid", "-"),
    ("dashed", "--"),
    ("dashdot", "-."),
    ("dotted", ":")
]

for ax, (name, style) in zip(axes.flat, styles):
    # linestyle sets the dash pattern; linewidth sets thickness in points
    ax.plot(x, np.sin(x), linestyle=style, linewidth=2, color="steelblue")
    ax.set_title(f"linestyle='{style}' ({name})")
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
