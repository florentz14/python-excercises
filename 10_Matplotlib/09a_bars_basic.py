# -------------------------------------------------
# File Name: 09a_bars_basic.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Basic vertical bar chart (programming languages).
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# =========================================================================
# Basic vertical bar chart
# =========================================================================

categories = ["Python", "JavaScript", "Java", "C++", "Go"]
values = [92, 78, 65, 55, 48]

plt.figure(figsize=(7, 5))
plt.bar(categories, values, color="steelblue", edgecolor="black")  # bar() creates vertical bars; edgecolor outlines each bar
plt.title("Programming Language Popularity")
plt.xlabel("Language")
plt.ylabel("Score")
plt.show()
