# -------------------------------------------------
# File Name: 01_pyplot_intro.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Pyplot Introduction.
#              Basics of importing matplotlib, creating simple
#              plots, multiple lines, saving figures, and the
#              object-oriented vs pyplot interface.
# -------------------------------------------------
"""
Matplotlib - 01: Pyplot Introduction
=====================================
Description: Matplotlib is the most popular Python plotting library.
             pyplot is its module for creating figures and plots.
             This file covers the basics: importing, creating simple
             plots, and understanding the figure/axes structure.
"""

import matplotlib.pyplot as plt  # "plt" is the standard alias for matplotlib.pyplot

# =========================================================================
# Basic plot with plt.plot()
# =========================================================================

# If you provide a single list, it becomes the Y values (X = 0, 1, 2...)
plt.figure(figsize=(8, 4))  # Create a new figure; figsize=(width, height) in inches

plt.subplot(1, 2, 1)  # Select subplot: (rows, cols, index) — index starts at 1
plt.plot([10, 20, 15, 25, 30])
plt.title("Y values only (X = auto)")

# If you provide two lists, first is X, second is Y
plt.subplot(1, 2, 2)
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("X and Y values")

plt.tight_layout()  # Automatically adjust spacing to prevent overlapping
plt.show()  # Render and display the figure window

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
fig, ax = plt.subplots(figsize=(6, 4))  # subplots() returns a Figure and Axes object for OOP control
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
ax.set_title("Object-Oriented Style")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
plt.show()

# --- Quick reference of the most common pyplot functions ---
print("\n--- Summary ---")
print("import matplotlib.pyplot as plt  -> Import the module")
print("plt.plot(x, y)                   -> Create a line plot")
print("plt.title('Title')               -> Set the title")
print("plt.xlabel('X') / plt.ylabel('Y')-> Set axis labels")
print("plt.legend()                     -> Show legend")
print("plt.show()                       -> Display the plot")
print("plt.savefig('file.png')          -> Save to file")
