# -------------------------------------------------
# File Name: 06a_grid_basic.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Basic grid on/off.
# -------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 7, 4, 9, 1, 6, 3]

# =========================================================================
# Basic grid
# =========================================================================

plt.figure(figsize=(6, 4))
plt.plot(x, y, "b-o")
plt.title("Basic Grid")
plt.grid(True)  # Enable grid on both axes; plt.grid() also works
plt.show()
