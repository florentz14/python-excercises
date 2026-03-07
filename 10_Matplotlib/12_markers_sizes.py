# -------------------------------------------------
# File Name: 03c_markers_sizes.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Marker Sizes — different markersize values.
# -------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [2, 4, 3, 5, 7, 6, 8]

# Demonstrate how markersize affects the visual weight of points
plt.figure(figsize=(8, 4))
sizes = [5, 10, 15, 20]
for i, size in enumerate(sizes):
    plt.plot(x, [v + i * 3 for v in y], marker="o", markersize=size,
             label=f"markersize={size}")
plt.title("Different Marker Sizes")
plt.legend()
plt.show()
