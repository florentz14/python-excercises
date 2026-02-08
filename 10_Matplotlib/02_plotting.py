"""
Matplotlib - 02: Plotting
=========================
Description: Plotting data points using plt.plot(). Covers plotting
             single and multiple datasets, default vs custom X values,
             formatting shortcuts, and plotting from different data types.
"""

import matplotlib.pyplot as plt

# =========================================================================
# Basic plotting with two points
# =========================================================================

# plot() draws a line from point to point
# Point 1: (1, 3), Point 2: (8, 10)
plt.figure(figsize=(6, 4))
plt.plot([1, 8], [3, 10])
plt.title("Line Between Two Points")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# =========================================================================
# Plotting without a line (only markers)
# =========================================================================

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 7, 4, 9, 1, 6, 3]

plt.figure(figsize=(6, 4))
plt.plot(x, y, "o")  # "o" = circle markers, no line
plt.title("Points Only (No Line)")
plt.show()

# =========================================================================
# Multiple lines with different styles
# =========================================================================

x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]     # quadratic
y2 = [0, 1, 2, 3, 4, 5]       # linear
y3 = [25, 16, 9, 4, 1, 0]     # reverse quadratic

plt.figure(figsize=(7, 5))
plt.plot(x, y1, "r-o", label="Quadratic")    # red, solid, circles
plt.plot(x, y2, "g--s", label="Linear")      # green, dashed, squares
plt.plot(x, y3, "b:^", label="Reverse")      # blue, dotted, triangles
plt.title("Multiple Lines with Format Strings")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

# =========================================================================
# Format string shortcuts: 'color marker line'
# =========================================================================
# Colors:  r=red, g=green, b=blue, c=cyan, m=magenta, y=yellow, k=black
# Markers: o=circle, s=square, ^=triangle, D=diamond, *=star, +=plus
# Lines:   - =solid, --=dashed, -.=dash-dot, : =dotted

print("Format string examples:")
print("  'ro'   -> red circles (no line)")
print("  'g--'  -> green dashed line")
print("  'b-o'  -> blue solid line with circles")
print("  'k:s'  -> black dotted line with squares")

# =========================================================================
# Plotting with keyword arguments (more control)
# =========================================================================

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure(figsize=(6, 4))
plt.plot(x, y,
         color="purple",
         linewidth=2.5,
         linestyle="--",
         marker="D",
         markersize=8,
         markerfacecolor="yellow",
         markeredgecolor="purple",
         label="Prime numbers")
plt.title("Plot with Keyword Arguments")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# =========================================================================
# Plotting from a dictionary
# =========================================================================

data = {"day": [1, 2, 3, 4, 5, 6, 7],
        "temperature": [72, 75, 71, 78, 82, 79, 85]}

plt.figure(figsize=(6, 4))
plt.plot("day", "temperature", data=data, marker="o", color="tomato")
plt.title("Weekly Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature (F)")
plt.grid(True, alpha=0.3)
plt.show()
