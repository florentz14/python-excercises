# -------------------------------------------------
# File Name: 10f_hist_cumulative.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Cumulative Histogram — running total
#              of frequency counts.
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# Fix seed so the random data is the same every time
np.random.seed(42)
# Normal distribution: mean=170 cm, std=10 cm, 250 samples
data = np.random.normal(loc=170, scale=10, size=250)

plt.figure(figsize=(7, 5))
# Each bar shows the total count up to that bin (running total)
plt.hist(data, bins=25, cumulative=True, color="purple",
         edgecolor="black", alpha=0.7)
plt.title("Cumulative Histogram")
plt.xlabel("Height (cm)")
plt.ylabel("Cumulative Frequency")
plt.grid(True, alpha=0.3)
plt.show()
