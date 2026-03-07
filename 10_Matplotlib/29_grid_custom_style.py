# -------------------------------------------------
# File Name: 06c_grid_custom_style.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Grid style: color, linestyle, linewidth, alpha.
# -------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 7, 4, 9, 1, 6, 3]

# =========================================================================
# Grid style customization
# =========================================================================

plt.figure(figsize=(7, 5))
plt.plot(x, y, "b-o", markersize=8, linewidth=2)

plt.grid(True,
         color="gray",        # Grid line color
         linestyle="--",      # Line style: '-', '--', '-.', ':'
         linewidth=0.5,       # Line width
         alpha=0.7)           # Transparency

plt.title("Customized Grid Style")
plt.show()
