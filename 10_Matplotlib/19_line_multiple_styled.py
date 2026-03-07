# -------------------------------------------------
# File Name: 04d_line_multiple_styled.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Multiple styled lines (sin, cos, sin*cos).
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)

# =========================================================================
# Multiple lines with different styles
# =========================================================================

plt.figure(figsize=(8, 5))
plt.plot(x, np.sin(x), "r-", linewidth=2, label="sin(x)")
plt.plot(x, np.cos(x), "b--", linewidth=2, label="cos(x)")
plt.plot(x, np.sin(x) * np.cos(x), "g-.", linewidth=2, label="sin(x)*cos(x)")
plt.title("Multiple Styled Lines")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
