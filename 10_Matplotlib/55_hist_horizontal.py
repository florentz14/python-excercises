# -------------------------------------------------
# File Name: 10e_hist_horizontal.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Horizontal histogram.
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# Generate random data (normal distribution)
np.random.seed(42)  # Fix seed so the random data is the same every time
data = np.random.normal(loc=170, scale=10, size=250)  # Normal distribution: mean=170 cm, std=10 cm, 250 samples

plt.figure(figsize=(7, 5))
plt.hist(data, bins=15, orientation="horizontal", color="forestgreen", edgecolor="black")  # orientation="horizontal" flips the histogram so bars extend horizontally
plt.title("Horizontal Histogram")
plt.xlabel("Frequency")
plt.ylabel("Height (cm)")
plt.show()
