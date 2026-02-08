# -------------------------------------------------
# File Name: 10d_hist_overlapping.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Multiple overlapping histograms (two groups).
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
group_a = np.random.normal(65, 8, 200)   # Simulate 200 exam scores with mean=65, std=8
group_b = np.random.normal(75, 10, 200)  # Exam scores group B

plt.figure(figsize=(7, 5))
plt.hist(group_a, bins=20, alpha=0.5, color="red", edgecolor="black", label="Group A")  # alpha=0.5 makes bars semi-transparent so both histograms are visible
plt.hist(group_b, bins=20, alpha=0.5, color="blue", edgecolor="black", label="Group B")
plt.title("Overlapping Histograms")
plt.xlabel("Exam Score")
plt.ylabel("Frequency")
plt.legend()
plt.show()
