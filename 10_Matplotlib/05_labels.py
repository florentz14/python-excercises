# -------------------------------------------------
# File Name: 05_labels.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Labels, Titles, and Annotations.
#              Add titles, axis labels, custom fonts, legend
#              positioning, text annotations with arrows, and
#              custom tick labels.
# -------------------------------------------------
"""
Matplotlib - 05: Labels and Titles
====================================
Description: Add titles, axis labels, text annotations, and legends
             to make plots informative and professional.
"""

import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 5, 4, 6, 8]

# =========================================================================
# Basic labels and title
# =========================================================================

plt.figure(figsize=(7, 5))  # Create a 7x5 inch figure for the basic labels demo
plt.plot(x, y, "b-o")

plt.title("Monthly Sales Report")     # Title
plt.xlabel("Month")                    # X-axis label
plt.ylabel("Sales (thousands)")        # Y-axis label

plt.show()

# =========================================================================
# Customize font: size, weight, family, color
# =========================================================================

plt.figure(figsize=(7, 5))
plt.plot(x, y, "r-s", markersize=8)

plt.title("Customized Labels",
          fontsize=20,
          fontweight="bold",
          color="darkblue",
          fontfamily="serif",
          pad=15)  # padding from the plot

plt.xlabel("X Axis",
           fontsize=14,
           fontweight="bold",
           color="darkgreen")

plt.ylabel("Y Axis",
           fontsize=14,
           fontweight="bold",
           color="darkred")

plt.show()

# =========================================================================
# Title position (loc parameter)
# =========================================================================

fig, axes = plt.subplots(1, 3, figsize=(12, 4))  # Three subplots to compare title alignment positions

axes[0].plot(x, y)
axes[0].set_title("Left Title", loc="left")  # loc="left" aligns the title to the left edge of the axes

axes[1].plot(x, y)
axes[1].set_title("Center Title (default)", loc="center")

axes[2].plot(x, y)
axes[2].set_title("Right Title", loc="right")

plt.tight_layout()
plt.show()

# =========================================================================
# Legend
# =========================================================================

plt.figure(figsize=(7, 5))
plt.plot(x, y, "b-o", label="Product A")
plt.plot(x, [v * 1.5 for v in y], "r-s", label="Product B")
plt.plot(x, [v * 0.7 for v in y], "g-^", label="Product C")

plt.title("Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")

# Legend with location control
# legend() creates a box showing which line is which
plt.legend(loc="upper left",           # Position
           fontsize=11,                 # Font size
           framealpha=0.9,              # Background transparency
           edgecolor="gray",            # Border color
           title="Products",            # Legend title
           title_fontsize=12)

plt.grid(True, alpha=0.3)
plt.show()

# Legend locations: 'upper left', 'upper right', 'lower left', 'lower right',
#                   'center', 'best' (auto), or numeric (0-10)

# =========================================================================
# Text annotations on the plot
# =========================================================================

plt.figure(figsize=(7, 5))
plt.plot(x, y, "b-o", markersize=8)

# Add text at a specific data point
# annotate() adds text with an optional arrow pointing to a data point
plt.annotate("Peak!",
             xy=(5, 6),                # Point to annotate
             xytext=(3.5, 7),          # Text position
             fontsize=12,
             fontweight="bold",
             color="red",
             arrowprops=dict(arrowstyle="->", color="red", lw=2))  # arrowprops dict controls the arrow style, color, and width

# Add plain text (no arrow)
plt.text(1.5, 7.5, "Monthly Report 2025",
         fontsize=14, fontweight="bold",
         bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.8))  # bbox draws a rounded box behind the text for readability

plt.title("Annotations and Text")
plt.xlabel("Month")
plt.ylabel("Value")
plt.grid(True, alpha=0.3)
plt.show()

# =========================================================================
# Tick labels customization
# =========================================================================

plt.figure(figsize=(7, 5))
plt.plot(x, y, "b-o")

# Custom tick labels
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
plt.xticks(x, months, fontsize=11, rotation=45)  # xticks() replaces numeric tick positions with custom labels
plt.yticks(fontsize=11)

plt.title("Custom Tick Labels")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
