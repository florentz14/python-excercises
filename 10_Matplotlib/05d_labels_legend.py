# -------------------------------------------------
# File Name: 05d_labels_legend.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Legend — positioning, font, border, and title.
# -------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 5, 4, 6, 8]

plt.figure(figsize=(7, 5))
plt.plot(x, y, "b-o", label="Product A")
plt.plot(x, [v * 1.5 for v in y], "r-s", label="Product B")
plt.plot(x, [v * 0.7 for v in y], "g-^", label="Product C")

plt.title("Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")

# legend() creates a box showing which line is which
plt.legend(loc="upper left",           # Position
           fontsize=11,                 # Font size
           framealpha=0.9,              # Background transparency
           edgecolor="gray",            # Border color
           title="Products",            # Legend title
           title_fontsize=12)

plt.grid(True, alpha=0.3)
plt.show()

# Legend locations: 'upper left', 'upper right', 'lower left', 'lower right',
#                   'center', 'best' (auto), or numeric (0-10)
