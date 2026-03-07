# -------------------------------------------------
# File Name: 05e_labels_annotations.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Text annotations with arrows + plain text box.
# -------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 5, 4, 6, 8]

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
