# -------------------------------------------------
# File Name: 02b_plotting_markers_only.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Points only, no line ("o" format).
# -------------------------------------------------

import matplotlib.pyplot as plt

# =========================================================================
# Plotting without a line (only markers)
# =========================================================================

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 7, 4, 9, 1, 6, 3]

plt.figure(figsize=(6, 4))
plt.plot(x, y, "o")  # Format string "o" = circle markers only, no connecting line
plt.title("Points Only (No Line)")
plt.show()
