# -------------------------------------------------
# File Name: 11c_pie_customized.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Customized pie (colors, explode, shadow, startangle).
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

labels = ["Python", "JavaScript", "Java", "C++", "Other"]
sizes = [35, 25, 20, 10, 10]
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
