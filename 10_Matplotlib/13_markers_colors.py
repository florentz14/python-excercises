# -------------------------------------------------
# File Name: 03d_markers_colors.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Marker Colors — face color, edge color,
#              and hollow markers (3 subplots).
# -------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [2, 4, 3, 5, 7, 6, 8]

plt.figure(figsize=(10, 5))

# Default marker colors
plt.subplot(1, 3, 1)
plt.plot(x, y, "o-", markersize=12)
plt.title("Default")

# Custom face color and edge color
plt.subplot(1, 3, 2)
plt.plot(x, y, "o-", markersize=12,
         markerfacecolor="yellow",
         markeredgecolor="red",
         markeredgewidth=2)  # Controls the thickness of the marker border
plt.title("mfc=yellow, mec=red")

# Hollow markers (face = none)
plt.subplot(1, 3, 3)
plt.plot(x, y, "o-", markersize=12,
         markerfacecolor="none",  # Setting face to "none" creates hollow/unfilled markers
         markeredgecolor="blue",
         markeredgewidth=2)
plt.title("Hollow (mfc=none)")

plt.tight_layout()
plt.show()
