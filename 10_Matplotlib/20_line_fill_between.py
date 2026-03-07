# -------------------------------------------------
# File Name: 04e_line_fill_between.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Lines with fill_between and alpha transparency.
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)

# =========================================================================
# Styled line with transparency (alpha)
# =========================================================================

plt.figure(figsize=(7, 5))

# Fill between with alpha
y1 = np.sin(x)
plt.plot(x, y1, "b-", linewidth=2)
# fill_between() shades the area between a curve and y=0
plt.fill_between(x, y1, alpha=0.2, color="blue")

y2 = np.cos(x)
plt.plot(x, y2, "r-", linewidth=2)
plt.fill_between(x, y2, alpha=0.2, color="red")

plt.title("Lines with Fill (alpha transparency)")
plt.grid(True, alpha=0.3)
plt.show()
