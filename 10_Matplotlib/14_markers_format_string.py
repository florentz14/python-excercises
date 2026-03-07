# -------------------------------------------------
# File Name: 03e_markers_format_string.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Format string shortcut with markers (r*-, g^--, bs:).
# -------------------------------------------------

import matplotlib.pyplot as plt

# =========================================================================
# Format string shortcut with markers
# =========================================================================

x = [1, 2, 3, 4, 5, 6, 7]
y = [2, 4, 3, 5, 7, 6, 8]

plt.figure(figsize=(8, 5))
plt.plot(x, y, "r*-", markersize=15, label="r*- (red, star, solid)")
plt.plot(x, [v - 1 for v in y], "g^--", markersize=10, label="g^-- (green, triangle, dashed)")
plt.plot(x, [v - 2 for v in y], "bs:", markersize=8, label="bs: (blue, square, dotted)")
plt.title("Markers with Format Strings")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
