# -------------------------------------------------
# File Name: 10_markers_basic.py
# Author: Florentino Báez
# Date: 10_Matplotlib
# Description: Default circle marker.
# -------------------------------------------------

import matplotlib.pyplot as plt

# =========================================================================
# Basic markers
# =========================================================================

x = [1, 2, 3, 4, 5, 6, 7]
y = [2, 4, 3, 5, 7, 6, 8]

plt.figure(figsize=(6, 4))
plt.plot(x, y, marker="o")  # Default circle marker
plt.title("Default Circle Marker")
plt.show()
