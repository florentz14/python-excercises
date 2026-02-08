# -------------------------------------------------
# File Name: 09g_bars_error.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Bar chart with error bars (yerr, capsize).
# -------------------------------------------------

import matplotlib.pyplot as plt

# =========================================================================
# Bar chart with error bars
# =========================================================================

categories = ["Python", "JavaScript", "Java", "C++", "Go"]
means = [85, 72, 90, 68, 95]
errors = [3, 5, 2, 7, 4]

plt.figure(figsize=(7, 5))
plt.bar(categories, means, yerr=errors, capsize=5,  # yerr adds vertical error bars; capsize sets the width of end caps
        color="steelblue", edgecolor="black", alpha=0.8)
plt.title("Bar Chart with Error Bars")
plt.ylabel("Score")
plt.grid(axis="y", alpha=0.3)
plt.show()
