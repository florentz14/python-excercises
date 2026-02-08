# -------------------------------------------------
# File Name: 04c_line_colors.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Line Colors — named, hex, and RGB colors.
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np  # numpy for mathematical functions (sin, cos) and array generation

x = np.linspace(0, 10, 50)  # Generate 50 evenly spaced values from 0 to 10

plt.figure(figsize=(8, 5))

# Named colors
plt.plot(x, np.sin(x), color="red", linewidth=2, label="red")
plt.plot(x, np.sin(x + 1), color="steelblue", linewidth=2, label="steelblue")
plt.plot(x, np.sin(x + 2), color="forestgreen", linewidth=2, label="forestgreen")

# Hex color code (RGB): FF=red, 66=green, 00=blue
plt.plot(x, np.sin(x + 3), color="#FF6600", linewidth=2, label="#FF6600")

# RGB tuple with values 0.0-1.0 (purple)
plt.plot(x, np.sin(x + 4), color=(0.5, 0.0, 0.8), linewidth=2, label="(0.5, 0.0, 0.8)")

plt.title("Line Colors")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Color shortcuts reference
print("Color shortcuts:")
print("  'r' -> red        'g' -> green      'b' -> blue")
print("  'c' -> cyan       'm' -> magenta    'y' -> yellow")
print("  'k' -> black      'w' -> white")
