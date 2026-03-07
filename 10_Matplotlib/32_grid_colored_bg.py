# -------------------------------------------------
# File Name: 06f_grid_colored_bg.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Grid with colored background. Includes print summary block.
# -------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 7, 4, 9, 1, 6, 3]

# =========================================================================
# Grid with colored background
# =========================================================================

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(x, y, "r-o", markersize=8, linewidth=2)

ax.set_facecolor("#f0f0f0")  # Set axes background to light gray; white grid lines stand out on it
ax.grid(True, color="white", linewidth=1.5)  # White grid lines on gray background (clean dashboard look)

ax.set_title("Grid with Background Color")
plt.show()

print("\n--- Grid Summary ---")
print("plt.grid(True)                          -> Enable grid")
print("plt.grid(axis='x')                      -> X-axis only")
print("plt.grid(color='gray', linestyle='--')  -> Custom style")
print("ax.grid(which='major')                  -> Major grid only")
print("ax.grid(which='minor')                  -> Minor grid only")
print("ax.grid(which='both')                   -> Both grids")
