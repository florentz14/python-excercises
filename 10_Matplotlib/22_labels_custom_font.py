# -------------------------------------------------
# File Name: 05b_labels_custom_font.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Custom font size, weight, family, color.
# -------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 5, 4, 6, 8]

# =========================================================================
# Customize font: size, weight, family, color
# =========================================================================

plt.figure(figsize=(7, 5))
plt.plot(x, y, "r-s", markersize=8)

plt.title("Customized Labels",
          fontsize=20,
          fontweight="bold",
          color="darkblue",
          fontfamily="serif",
          pad=15)  # padding from the plot

plt.xlabel("X Axis",
           fontsize=14,
           fontweight="bold",
           color="darkgreen")

plt.ylabel("Y Axis",
           fontsize=14,
           fontweight="bold",
           color="darkred")

plt.show()
