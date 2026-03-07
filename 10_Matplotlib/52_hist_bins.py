# -------------------------------------------------
# File Name: 10b_hist_bins.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Different bin counts (5, 15, 50) in 1x3 subplots.
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# Generate random data (normal distribution)
np.random.seed(42)  # Fix seed so the random data is the same every time
data = np.random.normal(loc=170, scale=10, size=250)  # Normal distribution: mean=170 cm, std=10 cm, 250 samples

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

for ax, bins in zip(axes, [5, 15, 50]):  # Compare how different bin counts affect histogram appearance
    ax.hist(data, bins=bins, color="steelblue", edgecolor="black")
    ax.set_title(f"bins={bins}")
    ax.set_xlabel("Height (cm)")
    ax.set_ylabel("Frequency")

plt.suptitle("Effect of Bin Count", fontsize=14)
plt.tight_layout()
plt.show()
