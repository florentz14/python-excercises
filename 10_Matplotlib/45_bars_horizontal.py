# -------------------------------------------------
# File Name: 09b_bars_horizontal.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Horizontal bar chart (barh).
# -------------------------------------------------

import matplotlib.pyplot as plt

# =========================================================================
# Horizontal bar chart (barh)
# =========================================================================

categories = ["Python", "JavaScript", "Java", "C++", "Go"]
values = [92, 78, 65, 55, 48]

plt.figure(figsize=(7, 5))
plt.barh(categories, values, color="coral", edgecolor="black")  # barh() creates horizontal bars (h = horizontal)
plt.title("Horizontal Bar Chart")
plt.xlabel("Score")
plt.show()
