"""
Matplotlib - 07: Subplots
=========================
Description: Display multiple plots in one figure using subplots.
             Arrange plots in rows and columns for comparison.
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)

# =========================================================================
# Basic: Two subplots side by side (1 row, 2 columns)
# =========================================================================

plt.figure(figsize=(10, 4))

# subplot(rows, cols, index)
plt.subplot(1, 2, 1)
plt.plot(x, np.sin(x), "b-")
plt.title("sin(x)")
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(x, np.cos(x), "r-")
plt.title("cos(x)")
plt.grid(True, alpha=0.3)

plt.suptitle("Two Subplots (1 row, 2 cols)", fontsize=14)
plt.tight_layout()
plt.show()

# =========================================================================
# Stacked subplots (2 rows, 1 column)
# =========================================================================

plt.figure(figsize=(7, 6))

plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x), "b-", linewidth=2)
plt.title("sin(x)")
plt.grid(True, alpha=0.3)

plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x), "r-", linewidth=2)
plt.title("cos(x)")
plt.grid(True, alpha=0.3)

plt.suptitle("Stacked Subplots (2 rows, 1 col)", fontsize=14)
plt.tight_layout()
plt.show()

# =========================================================================
# Grid of subplots (2 rows, 3 columns)
# =========================================================================

fig, axes = plt.subplots(2, 3, figsize=(14, 8))
fig.suptitle("2x3 Grid of Subplots", fontsize=16)

functions = [
    (np.sin, "sin(x)", "blue"),
    (np.cos, "cos(x)", "red"),
    (np.tan, "tan(x)", "green"),
    (lambda x: np.sin(2*x), "sin(2x)", "purple"),
    (lambda x: np.cos(2*x), "cos(2x)", "orange"),
    (lambda x: np.sin(x)**2, "sin^2(x)", "brown")
]

for ax, (func, title, color) in zip(axes.flat, functions):
    y = func(x)
    if title == "tan(x)":
        y = np.clip(y, -5, 5)  # Clip tan to avoid extreme values
    ax.plot(x, y, color=color, linewidth=2)
    ax.set_title(title)
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# =========================================================================
# Subplots with different sizes using GridSpec
# =========================================================================

fig = plt.figure(figsize=(10, 6))

# Big plot on the left
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(x, np.sin(x), "b-", linewidth=2)
ax1.set_title("Main Plot (Large)")
ax1.grid(True, alpha=0.3)

# Two small plots stacked on the right
ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(x, np.cos(x), "r-")
ax2.set_title("Top Right")
ax2.grid(True, alpha=0.3)

ax3 = fig.add_subplot(2, 2, 4)
ax3.plot(x, np.sin(x) * np.cos(x), "g-")
ax3.set_title("Bottom Right")
ax3.grid(True, alpha=0.3)

plt.suptitle("Mixed Layout", fontsize=14)
plt.tight_layout()
plt.show()

# =========================================================================
# Sharing axes between subplots
# =========================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4), sharey=True)

ax1.plot(x, np.sin(x), "b-")
ax1.set_title("sin(x)")
ax1.set_ylabel("y")
ax1.grid(True, alpha=0.3)

ax2.plot(x, np.cos(x), "r-")
ax2.set_title("cos(x)")
ax2.grid(True, alpha=0.3)
# Note: Y-axis is shared, so labels appear only on the left

plt.suptitle("Shared Y-Axis", fontsize=14)
plt.tight_layout()
plt.show()

print("\n--- Subplot Summary ---")
print("plt.subplot(rows, cols, index)  -> Select subplot position")
print("fig, axes = plt.subplots(r, c)  -> Create grid of axes")
print("plt.suptitle('Title')           -> Title for entire figure")
print("plt.tight_layout()              -> Auto-adjust spacing")
print("sharey=True / sharex=True       -> Share axis between subplots")
