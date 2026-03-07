# -------------------------------------------------
# File Name: 11d_pie_legend.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Pie with legend instead of slice labels.
# -------------------------------------------------

import matplotlib.pyplot as plt

labels = ["Python", "JavaScript", "Java", "C++", "Other"]
sizes = [35, 25, 20, 10, 10]
colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"]

plt.figure(figsize=(7, 6))
wedges, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(wedges, labels, title="Languages",
           loc="center left", bbox_to_anchor=(1, 0.5))  # Place legend at x=1 (right edge), y=0.5 (vertical center)
plt.title("Pie Chart with Legend")
plt.axis("equal")
plt.tight_layout()
plt.show()
