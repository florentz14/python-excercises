# -------------------------------------------------
# File Name: 51_hist_basic.py
# Author: Florentino Báez
# Date: 10_Matplotlib
# Description: Basic histogram (heights, 15 bins).
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# Generate random data (normal distribution)
np.random.seed(42)  # Fix seed so the random data is the same every time
data = np.random.normal(loc=170, scale=10, size=250)  # Normal distribution: mean=170 cm, std=10 cm, 250 samples

plt.figure(figsize=(7, 5))
plt.hist(data, bins=15, color="steelblue", edgecolor="black")  # bins=15 divides the data range into 15 equal intervals
plt.title("Height Distribution (250 people)")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.show()
