"""
Matplotlib - 06: Grid
=====================
Description: Add and customize grid lines to improve readability.
             Control which axis, style, color, and spacing of grid lines.
"""

import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 7, 4, 9, 1, 6, 3]

# =========================================================================
# Basic grid
# =========================================================================

plt.figure(figsize=(6, 4))
plt.plot(x, y, "b-o")
plt.title("Basic Grid")
plt.grid(True)  # or plt.grid()
plt.show()

# =========================================================================
# Grid on specific axis
# =========================================================================

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

# Both axes (default)
axes[0].plot(x, y, "b-o")
axes[0].grid(True, axis="both")
axes[0].set_title("axis='both' (default)")

# X-axis only
axes[1].plot(x, y, "r-s")
axes[1].grid(True, axis="x")
axes[1].set_title("axis='x'")

# Y-axis only
axes[2].plot(x, y, "g-^")
axes[2].grid(True, axis="y")
axes[2].set_title("axis='y'")

plt.tight_layout()
plt.show()

# =========================================================================
# Grid style customization
# =========================================================================

plt.figure(figsize=(7, 5))
plt.plot(x, y, "b-o", markersize=8, linewidth=2)

plt.grid(True,
         color="gray",        # Grid line color
         linestyle="--",      # Line style: '-', '--', '-.', ':'
         linewidth=0.5,       # Line width
         alpha=0.7)           # Transparency

plt.title("Customized Grid Style")
plt.show()

# =========================================================================
# Different grid line styles
# =========================================================================

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Grid Line Styles", fontsize=14)

styles = [
    ("Solid", "-", "steelblue"),
    ("Dashed", "--", "coral"),
    ("Dash-dot", "-.", "forestgreen"),
    ("Dotted", ":", "purple")
]

for ax, (name, style, color) in zip(axes.flat, styles):
    ax.plot(x, y, "ko-")
    ax.grid(True, linestyle=style, color=color, linewidth=1, alpha=0.7)
    ax.set_title(f"linestyle='{style}' ({name})")

plt.tight_layout()
plt.show()

# =========================================================================
# Major and minor grid lines
# =========================================================================

fig, ax = plt.subplots(figsize=(7, 5))

t = np.linspace(0, 2 * np.pi, 100)
ax.plot(t, np.sin(t), "b-", linewidth=2)

# Enable minor ticks
ax.minorticks_on()

# Major grid (thicker, darker)
ax.grid(which="major", color="gray", linestyle="-", linewidth=0.8, alpha=0.7)

# Minor grid (thinner, lighter)
ax.grid(which="minor", color="gray", linestyle=":", linewidth=0.4, alpha=0.4)

ax.set_title("Major and Minor Grid Lines")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
plt.show()

# =========================================================================
# Grid with colored background
# =========================================================================

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(x, y, "r-o", markersize=8, linewidth=2)

ax.set_facecolor("#f0f0f0")  # Light gray background
ax.grid(True, color="white", linewidth=1.5)  # White grid on gray

ax.set_title("Grid with Background Color")
plt.show()

print("\n--- Grid Summary ---")
print("plt.grid(True)                          -> Enable grid")
print("plt.grid(axis='x')                      -> X-axis only")
print("plt.grid(color='gray', linestyle='--')  -> Custom style")
print("ax.grid(which='major')                  -> Major grid only")
print("ax.grid(which='minor')                  -> Minor grid only")
print("ax.grid(which='both')                   -> Both grids")
