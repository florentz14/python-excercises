# -------------------------------------------------
# File Name: 11a_pie_basic.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Basic pie chart (programming languages).
# -------------------------------------------------

import matplotlib.pyplot as plt

labels = ["Python", "JavaScript", "Java", "C++", "Other"]
sizes = [35, 25, 20, 10, 10]

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels)  # Basic pie: sizes define slice proportions, labels name each slice
plt.title("Programming Language Usage")
plt.show()
