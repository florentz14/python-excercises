"""
Matplotlib - 03: Markers
========================
Description: Markers are used to highlight data points on a plot.
             Customize marker type, size, color, and edge properties.
"""

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

# =========================================================================
# Different marker types
# =========================================================================

fig, axes = plt.subplots(2, 3, figsize=(12, 8))
fig.suptitle("Common Marker Types", fontsize=14)

markers = [
    ("o", "Circle"),
    ("s", "Square"),
    ("^", "Triangle Up"),
    ("D", "Diamond"),
    ("*", "Star"),
    ("+", "Plus")
]

for ax, (marker, name) in zip(axes.flat, markers):
    ax.plot(x, y, marker=marker, markersize=10, linewidth=1.5)
    ax.set_title(f"marker='{marker}' ({name})")
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# =========================================================================
# All marker reference
# =========================================================================
print("Common markers:")
print("  'o' -> Circle       's' -> Square       '^' -> Triangle up")
print("  'v' -> Triangle dn  'D' -> Diamond      'd' -> Thin diamond")
print("  '*' -> Star         '+' -> Plus          'x' -> X")
print("  'p' -> Pentagon     'h' -> Hexagon       '.' -> Point")
print("  '|' -> Vline        '_' -> Hline")

# =========================================================================
# Marker size (markersize / ms)
# =========================================================================

plt.figure(figsize=(8, 4))
sizes = [5, 10, 15, 20]
for i, size in enumerate(sizes):
    plt.plot(x, [v + i * 3 for v in y], marker="o", markersize=size,
             label=f"markersize={size}")
plt.title("Different Marker Sizes")
plt.legend()
plt.show()

# =========================================================================
# Marker colors: markerfacecolor (mfc) and markeredgecolor (mec)
# =========================================================================

plt.figure(figsize=(10, 5))

# Default
plt.subplot(1, 3, 1)
plt.plot(x, y, "o-", markersize=12)
plt.title("Default")

# Custom face color
plt.subplot(1, 3, 2)
plt.plot(x, y, "o-", markersize=12,
         markerfacecolor="yellow",
         markeredgecolor="red",
         markeredgewidth=2)
plt.title("mfc=yellow, mec=red")

# Hollow markers (face = none)
plt.subplot(1, 3, 3)
plt.plot(x, y, "o-", markersize=12,
         markerfacecolor="none",
         markeredgecolor="blue",
         markeredgewidth=2)
plt.title("Hollow (mfc=none)")

plt.tight_layout()
plt.show()

# =========================================================================
# Format string shortcut with markers
# =========================================================================

plt.figure(figsize=(8, 5))
plt.plot(x, y, "r*-", markersize=15, label="r*- (red, star, solid)")
plt.plot(x, [v - 1 for v in y], "g^--", markersize=10, label="g^-- (green, triangle, dashed)")
plt.plot(x, [v - 2 for v in y], "bs:", markersize=8, label="bs: (blue, square, dotted)")
plt.title("Markers with Format Strings")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# =========================================================================
# Every Nth marker (markevery)
# =========================================================================

import numpy as np
x_dense = np.linspace(0, 10, 100)
y_dense = np.sin(x_dense)

plt.figure(figsize=(6, 4))
plt.plot(x_dense, y_dense, "b-o", markersize=6, markevery=10,
         label="markevery=10")
plt.title("Show Marker Every 10th Point")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
