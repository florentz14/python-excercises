# -------------------------------------------------
# File Name: 10_histograms.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Histograms.
#              Frequency distribution of continuous data. Bin
#              count, density normalization, overlapping groups,
#              cumulative, horizontal, and step histograms.
# -------------------------------------------------

"""
Matplotlib - 10: Histograms
============================
Description: Histograms show the frequency distribution of data.
             Unlike bar charts, histograms work with continuous data
             grouped into bins (intervals).
"""

import matplotlib.pyplot as plt
import numpy as np

# =========================================================================
# Basic histogram
# =========================================================================

# Generate random data (normal distribution)
np.random.seed(42)  # Fix seed so the random data is the same every time
data = np.random.normal(loc=170, scale=10, size=250)  # Normal distribution: mean=170 cm, std=10 cm, 250 samples

plt.figure(figsize=(7, 5))
plt.hist(data, bins=15, color="steelblue", edgecolor="black")  # bins=15 divides the data range into 15 equal intervals
plt.title("Height Distribution (250 people)")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.show()

# =========================================================================
# Different number of bins
# =========================================================================

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

for ax, bins in zip(axes, [5, 15, 50]):  # Compare how different bin counts affect histogram appearance
    ax.hist(data, bins=bins, color="steelblue", edgecolor="black")
    ax.set_title(f"bins={bins}")
    ax.set_xlabel("Height (cm)")
    ax.set_ylabel("Frequency")

plt.suptitle("Effect of Bin Count", fontsize=14)
plt.tight_layout()
plt.show()

# =========================================================================
# Histogram with density (normalized, area = 1)
# =========================================================================

plt.figure(figsize=(7, 5))
plt.hist(data, bins=20, density=True, color="coral", edgecolor="black", alpha=0.7)  # density=True normalizes so total area under histogram = 1

# Overlay the theoretical normal distribution curve
x_curve = np.linspace(data.min(), data.max(), 100)
from scipy.stats import norm  # scipy.stats.norm provides normal distribution PDF
plt.plot(x_curve, norm.pdf(x_curve, 170, 10), "b-", linewidth=2, label="Normal curve")  # Overlay the theoretical bell curve (mean=170, std=10)

plt.title("Density Histogram with Normal Curve")
plt.xlabel("Height (cm)")
plt.ylabel("Density")
plt.legend()
plt.show()

# =========================================================================
# Multiple histograms overlapping
# =========================================================================

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

# =========================================================================
# Horizontal histogram
# =========================================================================

plt.figure(figsize=(7, 5))
plt.hist(data, bins=15, orientation="horizontal", color="forestgreen", edgecolor="black")  # orientation="horizontal" flips the histogram so bars extend horizontally
plt.title("Horizontal Histogram")
plt.xlabel("Frequency")
plt.ylabel("Height (cm)")
plt.show()

# =========================================================================
# Cumulative histogram
# =========================================================================

plt.figure(figsize=(7, 5))
plt.hist(data, bins=25, cumulative=True, color="purple",  # cumulative=True means each bar shows the total count up to that bin (running total)
         edgecolor="black", alpha=0.7)
plt.title("Cumulative Histogram")
plt.xlabel("Height (cm)")
plt.ylabel("Cumulative Frequency")
plt.grid(True, alpha=0.3)
plt.show()

# =========================================================================
# Step histogram (unfilled)
# =========================================================================

plt.figure(figsize=(7, 5))
plt.hist(data, bins=20, histtype="step", color="darkblue", linewidth=2)  # "step" draws only the outline without filling the bars
plt.hist(data, bins=20, histtype="stepfilled", color="skyblue", alpha=0.3)  # "stepfilled" draws filled area under the step outline
plt.title("Step Histogram")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.show()

print("\n--- Histogram Summary ---")
print("plt.hist(data, bins=N)           -> Basic histogram")
print("density=True                     -> Normalize (area=1)")
print("cumulative=True                  -> Cumulative histogram")
print("orientation='horizontal'         -> Horizontal bars")
print("histtype='step'                  -> Unfilled outline")
print("alpha=0.5                        -> Transparency for overlapping")
