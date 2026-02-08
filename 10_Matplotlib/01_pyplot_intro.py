"""
Matplotlib - 01: Pyplot Introduction
=====================================
Description: Matplotlib is the most popular Python plotting library.
             pyplot is its module for creating figures and plots.
             This file covers the basics: importing, creating simple
             plots, and understanding the figure/axes structure.
"""

import matplotlib.pyplot as plt

# =========================================================================
# Basic plot with plt.plot()
# =========================================================================

# If you provide a single list, it becomes the Y values (X = 0, 1, 2...)
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.plot([10, 20, 15, 25, 30])
plt.title("Y values only (X = auto)")

# If you provide two lists, first is X, second is Y
plt.subplot(1, 2, 2)
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("X and Y values")

plt.tight_layout()
plt.show()

# =========================================================================
# Multiple plots on the same figure
# =========================================================================

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]   # x squared
y2 = [1, 8, 27, 64, 125]  # x cubed

plt.figure(figsize=(6, 4))
plt.plot(x, y1, label="x^2")
plt.plot(x, y2, label="x^3")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Multiple Lines on One Plot")
plt.legend()
plt.show()

# =========================================================================
# Saving a figure to a file
# =========================================================================

plt.figure(figsize=(6, 4))
plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
plt.title("Saved Figure")
# plt.savefig("my_plot.png", dpi=150, bbox_inches="tight")
# Supported formats: png, jpg, svg, pdf
print("To save: plt.savefig('filename.png', dpi=150)")

plt.show()

# =========================================================================
# Figure and Axes (Object-Oriented approach)
# =========================================================================

# Method 1: pyplot interface (simple, used above)
# plt.plot(), plt.title(), plt.show()

# Method 2: Object-oriented (more control)
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
ax.set_title("Object-Oriented Style")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
plt.show()

print("\n--- Summary ---")
print("import matplotlib.pyplot as plt  -> Import the module")
print("plt.plot(x, y)                   -> Create a line plot")
print("plt.title('Title')               -> Set the title")
print("plt.xlabel('X') / plt.ylabel('Y')-> Set axis labels")
print("plt.legend()                     -> Show legend")
print("plt.show()                       -> Display the plot")
print("plt.savefig('file.png')          -> Save to file")
