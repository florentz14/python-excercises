# -------------------------------------------------
# File Name: 06d_grid_line_styles.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Different grid line styles (2x2 grid).
# -------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 7, 4, 9, 1, 6, 3]

# =========================================================================
# Different grid line styles
# =========================================================================

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Grid Line Styles", fontsize=14)

styles = [
    ("Solid", "-", "steelblue"),
    ("Dashed", "--", "coral"),
    ("Dash-dot", "-.", "forestgreen"),
    ("Dotted", ":", "purple")
]

for ax, (name, style, color) in zip(axes.flat, styles):
    ax.plot(x, y, "ko-")
    ax.grid(True, linestyle=style, color=color, linewidth=1, alpha=0.7)
    ax.set_title(f"linestyle='{style}' ({name})")

plt.tight_layout()
plt.show()
