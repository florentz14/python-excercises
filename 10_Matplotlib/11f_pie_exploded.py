# -------------------------------------------------
# File Name: 11f_pie_exploded.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Monthly expenses pie with all slices slightly exploded.
# -------------------------------------------------

import matplotlib.pyplot as plt

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
