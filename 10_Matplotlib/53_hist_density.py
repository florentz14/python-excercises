# -------------------------------------------------
# File Name: 10c_hist_density.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Density histogram with normal curve overlay.
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm  # scipy.stats.norm provides normal distribution PDF

# Generate random data (normal distribution)
np.random.seed(42)  # Fix seed so the random data is the same every time
data = np.random.normal(loc=170, scale=10, size=250)  # Normal distribution: mean=170 cm, std=10 cm, 250 samples

plt.figure(figsize=(7, 5))
plt.hist(data, bins=20, density=True, color="coral", edgecolor="black", alpha=0.7)  # density=True normalizes so total area under histogram = 1

# Overlay the theoretical normal distribution curve
x_curve = np.linspace(data.min(), data.max(), 100)
plt.plot(x_curve, norm.pdf(x_curve, 170, 10), "b-", linewidth=2, label="Normal curve")  # Overlay the theoretical bell curve (mean=170, std=10)

plt.title("Density Histogram with Normal Curve")
plt.xlabel("Height (cm)")
plt.ylabel("Density")
plt.legend()
plt.show()
