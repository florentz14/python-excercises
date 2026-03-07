# -------------------------------------------------
# File Name: 11g_pie_nested.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Nested pie chart (outer + inner ring).
# -------------------------------------------------

import matplotlib.pyplot as plt

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
