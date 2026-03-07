# -------------------------------------------------
# File Name: 09c_bars_custom_colors.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Custom colors with value labels on top.
# -------------------------------------------------

import matplotlib.pyplot as plt

# =========================================================================
# Custom bar colors (one per bar)
# =========================================================================

categories = ["Python", "JavaScript", "Java", "C++", "Go"]
values = [92, 78, 65, 55, 48]
colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"]

plt.figure(figsize=(7, 5))
bars = plt.bar(categories, values, color=colors, edgecolor="black", linewidth=0.8)  # Store bar objects in 'bars' to access their position/height later

# Add value labels on top of each bar
# Place value labels centered on top of each bar
for bar, val in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             str(val), ha="center", fontweight="bold")

plt.title("Bars with Custom Colors and Labels")
plt.ylabel("Score")
plt.show()
