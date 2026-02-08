"""
Matplotlib - 04: Line Styles
=============================
Description: Customize line appearance: style, width, color, and
             multiple lines. Control every aspect of how lines are drawn.
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)

# =========================================================================
# Line styles
# =========================================================================

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Line Styles", fontsize=14)

styles = [
    ("solid", "-"),
    ("dashed", "--"),
    ("dashdot", "-."),
    ("dotted", ":")
]

for ax, (name, style) in zip(axes.flat, styles):
    ax.plot(x, np.sin(x), linestyle=style, linewidth=2, color="steelblue")
    ax.set_title(f"linestyle='{style}' ({name})")
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# =========================================================================
# Line width (linewidth / lw)
# =========================================================================

plt.figure(figsize=(8, 5))
for width in [0.5, 1, 2, 3, 5]:
    plt.plot(x, np.sin(x + width), linewidth=width,
             label=f"linewidth={width}")
plt.title("Different Line Widths")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# =========================================================================
# Line colors
# =========================================================================

plt.figure(figsize=(8, 5))

# Named colors
plt.plot(x, np.sin(x), color="red", linewidth=2, label="red")
plt.plot(x, np.sin(x + 1), color="steelblue", linewidth=2, label="steelblue")
plt.plot(x, np.sin(x + 2), color="forestgreen", linewidth=2, label="forestgreen")

# Hex color
plt.plot(x, np.sin(x + 3), color="#FF6600", linewidth=2, label="#FF6600")

# RGB tuple (0-1 range)
plt.plot(x, np.sin(x + 4), color=(0.5, 0.0, 0.8), linewidth=2, label="(0.5, 0.0, 0.8)")

plt.title("Line Colors")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# =========================================================================
# Color shortcuts in format string
# =========================================================================

print("Color shortcuts:")
print("  'r' -> red        'g' -> green      'b' -> blue")
print("  'c' -> cyan       'm' -> magenta    'y' -> yellow")
print("  'k' -> black      'w' -> white")

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

# =========================================================================
# Styled line with transparency (alpha)
# =========================================================================

plt.figure(figsize=(7, 5))

# Fill between with alpha
y1 = np.sin(x)
plt.plot(x, y1, "b-", linewidth=2)
plt.fill_between(x, y1, alpha=0.2, color="blue")

y2 = np.cos(x)
plt.plot(x, y2, "r-", linewidth=2)
plt.fill_between(x, y2, alpha=0.2, color="red")

plt.title("Lines with Fill (alpha transparency)")
plt.grid(True, alpha=0.3)
plt.show()
