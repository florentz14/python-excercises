# -------------------------------------------------
# File Name: 11b_pie_percentages.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Pie with autopct percentages.
# -------------------------------------------------

import matplotlib.pyplot as plt

labels = ["Python", "JavaScript", "Java", "C++", "Other"]
sizes = [35, 25, 20, 10, 10]

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%")  # autopct formats the percentage shown on each slice (%1.1f = one decimal)
plt.title("With Percentages")
plt.show()
