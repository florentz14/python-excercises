# -------------------------------------------------
# File Name: 11_pie_charts.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Pie Charts.
#              Show proportions of a whole. Percentages, exploded
#              slices, donut charts, legends, nested pie, and
#              custom colors/shadows.
# -------------------------------------------------

"""
Matplotlib - 11: Pie Charts
============================
Description: Pie charts show proportions of a whole. Each slice
             represents a category's share of the total.
"""

import matplotlib.pyplot as plt

# =========================================================================
# Basic pie chart
# =========================================================================

labels = ["Python", "JavaScript", "Java", "C++", "Other"]
sizes = [35, 25, 20, 10, 10]

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels)  # Basic pie: sizes define slice proportions, labels name each slice
plt.title("Programming Language Usage")
plt.show()

# =========================================================================
# Pie chart with percentages
# =========================================================================

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%")  # autopct formats the percentage shown on each slice (%1.1f = one decimal)
plt.title("With Percentages")
plt.show()

# =========================================================================
# Customized pie chart
# =========================================================================

colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"]
explode = (0.1, 0, 0, 0, 0)  # Fraction to offset each slice from center; 0.1 pulls Python slice out

plt.figure(figsize=(7, 7))
wedges, texts, autotexts = plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    explode=explode,
    autopct="%1.1f%%",
    shadow=True,  # Adds a drop shadow behind the pie for a 3D effect
    startangle=90,  # Rotate pie so the first slice starts at the top (90 degrees)
    textprops={"fontsize": 11}
)

# Bold the percentage text
for autotext in autotexts:
    autotext.set_fontweight("bold")
    autotext.set_color("white")

plt.title("Customized Pie Chart", fontsize=14, fontweight="bold")
plt.axis("equal")  # Force equal aspect ratio so the pie is a perfect circle
plt.show()

# =========================================================================
# Pie chart with legend (instead of labels on slices)
# =========================================================================

plt.figure(figsize=(7, 6))
wedges, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(wedges, labels, title="Languages",
           loc="center left", bbox_to_anchor=(1, 0.5))  # Place legend at x=1 (right edge), y=0.5 (vertical center)
plt.title("Pie Chart with Legend")
plt.axis("equal")
plt.tight_layout()
plt.show()

# =========================================================================
# Donut chart (pie with a hole)
# =========================================================================

plt.figure(figsize=(7, 7))
wedges, texts, autotexts = plt.pie(
    sizes, labels=labels, colors=colors,
    autopct="%1.1f%%", startangle=90,
    pctdistance=0.8,  # Distance of % label from center (1.0 = edge, 0 = center)
    textprops={"fontsize": 10}
)

# Draw a white circle in the center
centre_circle = plt.Circle((0, 0), 0.55, fc="white")  # Create a white circle to place over the pie center (donut hole)
plt.gca().add_artist(centre_circle)  # gca() = get current axes; add_artist() overlays the circle

# Add text in the center
plt.text(0, 0, "2025\nSurvey", ha="center", va="center",
         fontsize=14, fontweight="bold")

plt.title("Donut Chart")
plt.axis("equal")
plt.show()

# =========================================================================
# Multiple exploded slices
# =========================================================================

expenses = [40, 25, 15, 10, 10]
exp_labels = ["Rent", "Food", "Transport", "Entertainment", "Savings"]
exp_colors = ["#FF9999", "#66B3FF", "#99FF99", "#FFCC99", "#FF6666"]
explode_all = (0.05, 0.05, 0.05, 0.05, 0.05)  # Small equal explode on all slices creates gaps between them

plt.figure(figsize=(7, 7))
plt.pie(expenses, labels=exp_labels, colors=exp_colors,
        explode=explode_all, autopct="%1.0f%%",
        startangle=140, shadow=True)
plt.title("Monthly Expenses Breakdown", fontsize=13)
plt.axis("equal")
plt.show()

# =========================================================================
# Nested pie chart (pie of pie)
# =========================================================================

fig, ax = plt.subplots(figsize=(7, 7))

# Outer ring
outer_sizes = [40, 30, 20, 10]
outer_labels = ["Web", "Mobile", "Desktop", "Other"]
outer_colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4"]

# Inner ring
inner_sizes = [20, 20, 15, 15, 10, 10, 10]
inner_colors = ["#FF9999", "#FF6666", "#7EDDD3", "#3DB8A1",
                "#6FC8E0", "#A8E6CF", "#DCEDC1"]

ax.pie(outer_sizes, labels=outer_labels, colors=outer_colors,
       radius=1.2, autopct="%1.0f%%", pctdistance=0.85,
       wedgeprops=dict(width=0.4, edgecolor="white"))  # width=0.4 makes a ring (not full disk); edgecolor separates slices

# Inner ring: smaller radius creates concentric rings
ax.pie(inner_sizes, colors=inner_colors,
       radius=0.8,
       wedgeprops=dict(width=0.4, edgecolor="white"))

ax.set_title("Nested Pie Chart", fontsize=14, pad=20)
plt.show()

print("\n--- Pie Chart Summary ---")
print("plt.pie(sizes, labels=labels)         -> Basic pie")
print("autopct='%1.1f%%'                     -> Show percentages")
print("explode=(0.1, 0, 0)                   -> Pull out a slice")
print("shadow=True                           -> Add shadow")
print("startangle=90                         -> Rotate start position")
print("plt.axis('equal')                     -> Ensure circular shape")
