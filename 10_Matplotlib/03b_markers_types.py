# -------------------------------------------------
# File Name: 03b_markers_types.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Different marker types (2x3 grid subplots). Includes print reference for common markers.
# -------------------------------------------------

import matplotlib.pyplot as plt

# =========================================================================
# Different marker types
# =========================================================================

x = [1, 2, 3, 4, 5, 6, 7]
y = [2, 4, 3, 5, 7, 6, 8]

fig, axes = plt.subplots(2, 3, figsize=(12, 8))  # Create a 2x3 grid of subplots; axes is a 2D numpy array
fig.suptitle("Common Marker Types", fontsize=14)

markers = [
    ("o", "Circle"),
    ("s", "Square"),
    ("^", "Triangle Up"),
    ("D", "Diamond"),
    ("*", "Star"),
    ("+", "Plus")
]

for ax, (marker, name) in zip(axes.flat, markers):  # axes.flat flattens the 2D array so we can iterate linearly
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
