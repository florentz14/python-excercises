"""
Matplotlib - 09: Bar Charts
============================
Description: Create vertical and horizontal bar charts. Customize
             colors, width, labels, and create grouped/stacked bars.
"""

import matplotlib.pyplot as plt
import numpy as np

# =========================================================================
# Basic vertical bar chart
# =========================================================================

categories = ["Python", "JavaScript", "Java", "C++", "Go"]
values = [92, 78, 65, 55, 48]

plt.figure(figsize=(7, 5))
plt.bar(categories, values, color="steelblue", edgecolor="black")
plt.title("Programming Language Popularity")
plt.xlabel("Language")
plt.ylabel("Score")
plt.show()

# =========================================================================
# Horizontal bar chart (barh)
# =========================================================================

plt.figure(figsize=(7, 5))
plt.barh(categories, values, color="coral", edgecolor="black")
plt.title("Horizontal Bar Chart")
plt.xlabel("Score")
plt.show()

# =========================================================================
# Custom bar colors (one per bar)
# =========================================================================

colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"]

plt.figure(figsize=(7, 5))
bars = plt.bar(categories, values, color=colors, edgecolor="black", linewidth=0.8)

# Add value labels on top of each bar
for bar, val in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             str(val), ha="center", fontweight="bold")

plt.title("Bars with Custom Colors and Labels")
plt.ylabel("Score")
plt.show()

# =========================================================================
# Bar width customization
# =========================================================================

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.bar(categories, values, width=0.3, color="steelblue")
plt.title("Thin bars (width=0.3)")

plt.subplot(1, 2, 2)
plt.bar(categories, values, width=0.9, color="coral")
plt.title("Wide bars (width=0.9)")

plt.tight_layout()
plt.show()

# =========================================================================
# Grouped bar chart (comparing two datasets)
# =========================================================================

labels = ["Q1", "Q2", "Q3", "Q4"]
product_a = [20, 35, 30, 35]
product_b = [25, 32, 34, 20]
product_c = [15, 25, 28, 30]

x_pos = np.arange(len(labels))
width = 0.25

plt.figure(figsize=(8, 5))
plt.bar(x_pos - width, product_a, width, label="Product A", color="#FF6B6B")
plt.bar(x_pos, product_b, width, label="Product B", color="#4ECDC4")
plt.bar(x_pos + width, product_c, width, label="Product C", color="#45B7D1")

plt.xticks(x_pos, labels)
plt.title("Quarterly Sales by Product")
plt.xlabel("Quarter")
plt.ylabel("Sales (thousands)")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.show()

# =========================================================================
# Stacked bar chart
# =========================================================================

plt.figure(figsize=(7, 5))
plt.bar(labels, product_a, label="Product A", color="#FF6B6B")
plt.bar(labels, product_b, bottom=product_a, label="Product B", color="#4ECDC4")
plt.bar(labels, product_c,
        bottom=[a + b for a, b in zip(product_a, product_b)],
        label="Product C", color="#45B7D1")

plt.title("Stacked Bar Chart")
plt.xlabel("Quarter")
plt.ylabel("Total Sales")
plt.legend()
plt.show()

# =========================================================================
# Bar chart with error bars
# =========================================================================

means = [85, 72, 90, 68, 95]
errors = [3, 5, 2, 7, 4]

plt.figure(figsize=(7, 5))
plt.bar(categories, means, yerr=errors, capsize=5,
        color="steelblue", edgecolor="black", alpha=0.8)
plt.title("Bar Chart with Error Bars")
plt.ylabel("Score")
plt.grid(axis="y", alpha=0.3)
plt.show()
