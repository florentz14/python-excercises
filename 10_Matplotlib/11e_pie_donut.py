# -------------------------------------------------
# File Name: 11e_pie_donut.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Donut chart (pie with white circle center).
# -------------------------------------------------

import matplotlib.pyplot as plt

labels = ["Python", "JavaScript", "Java", "C++", "Other"]
sizes = [35, 25, 20, 10, 10]
colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"]

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
