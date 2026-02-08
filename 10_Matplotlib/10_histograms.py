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
np.random.seed(42)
data = np.random.normal(loc=170, scale=10, size=250)  # Heights in cm

plt.figure(figsize=(7, 5))
plt.hist(data, bins=15, color="steelblue", edgecolor="black")
plt.title("Height Distribution (250 people)")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.show()

# =========================================================================
# Different number of bins
# =========================================================================

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

for ax, bins in zip(axes, [5, 15, 50]):
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
plt.hist(data, bins=20, density=True, color="coral", edgecolor="black", alpha=0.7)

# Overlay the theoretical normal distribution curve
x_curve = np.linspace(data.min(), data.max(), 100)
from scipy.stats import norm
plt.plot(x_curve, norm.pdf(x_curve, 170, 10), "b-", linewidth=2, label="Normal curve")

plt.title("Density Histogram with Normal Curve")
plt.xlabel("Height (cm)")
plt.ylabel("Density")
plt.legend()
plt.show()

# =========================================================================
# Multiple histograms overlapping
# =========================================================================

group_a = np.random.normal(65, 8, 200)   # Exam scores group A
group_b = np.random.normal(75, 10, 200)  # Exam scores group B

plt.figure(figsize=(7, 5))
plt.hist(group_a, bins=20, alpha=0.5, color="red", edgecolor="black", label="Group A")
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
plt.hist(data, bins=15, orientation="horizontal", color="forestgreen", edgecolor="black")
plt.title("Horizontal Histogram")
plt.xlabel("Frequency")
plt.ylabel("Height (cm)")
plt.show()

# =========================================================================
# Cumulative histogram
# =========================================================================

plt.figure(figsize=(7, 5))
plt.hist(data, bins=25, cumulative=True, color="purple",
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
plt.hist(data, bins=20, histtype="step", color="darkblue", linewidth=2)
plt.hist(data, bins=20, histtype="stepfilled", color="skyblue", alpha=0.3)
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
