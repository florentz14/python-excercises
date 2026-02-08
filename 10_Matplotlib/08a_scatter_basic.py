# -------------------------------------------------
# File Name: 08a_scatter_basic.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Basic scatter plot (age vs speed).
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# =========================================================================
# Basic scatter plot
# =========================================================================

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

plt.figure(figsize=(6, 4))
plt.scatter(x, y)  # scatter() plots individual points without connecting lines
plt.title("Basic Scatter Plot")
plt.xlabel("Age")
plt.ylabel("Speed")
plt.show()
