# -------------------------------------------------
# File Name: 08b_scatter_two_datasets.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Compare two datasets (morning vs afternoon).
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# =========================================================================
# Compare two datasets
# =========================================================================

# Dataset 1
x1 = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y1 = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78]

# Dataset 2
x2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
y2 = [105, 95, 90, 85, 80, 75, 70, 65, 60, 55]

plt.figure(figsize=(7, 5))
plt.scatter(x1, y1, color="red", label="Morning", marker="o", s=80)  # s=80 sets the marker area in points^2; marker="o" uses circles
plt.scatter(x2, y2, color="blue", label="Afternoon", marker="s", s=80)
plt.title("Two Datasets Comparison")
plt.xlabel("Age")
plt.ylabel("Speed")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
