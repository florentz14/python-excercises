# -------------------------------------------------
# File Name: 01b_pyplot_multiple_lines.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Multiple lines on one plot (x^2, x^3).
# -------------------------------------------------

import matplotlib.pyplot as plt

# =========================================================================
# Multiple plots on the same figure
# =========================================================================

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]   # x squared
y2 = [1, 8, 27, 64, 125]  # x cubed

plt.figure(figsize=(6, 4))
# Each plot() call adds a new line to the same axes
plt.plot(x, y1, label="x^2")
plt.plot(x, y2, label="x^3")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Multiple Lines on One Plot")
plt.legend()  # Display legend using the 'label' parameter from each plot()
plt.show()
