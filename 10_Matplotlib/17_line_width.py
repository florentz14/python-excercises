# -------------------------------------------------
# File Name: 04b_line_width.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Different line widths (0.5 to 5).
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)

# =========================================================================
# Line width (linewidth / lw)
# =========================================================================

plt.figure(figsize=(8, 5))
for width in [0.5, 1, 2, 3, 5]:
    plt.plot(x, np.sin(x + width), linewidth=width,  # Shifting sin(x) by 'width' offsets curves so they don't overlap
             label=f"linewidth={width}")
plt.title("Different Line Widths")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
