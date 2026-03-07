# -------------------------------------------------
# File Name: 13_estadistico_multi.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Multi-Chart Statistical Analysis.
#              Side-by-side histogram and boxplot of the same
#              dataset using subplots for combined statistical
#              visualization.
# -------------------------------------------------

"""
Matplotlib - Example 7: Multiple statistical charts in one figure
====================================================================
Topic: Matplotlib (10_Matplotlib)
Description: subplots with histogram and boxplot of the same data.
"""

import matplotlib.pyplot as plt
# Only matplotlib needed — no extra libraries for this exercise

# Sample dataset: 15 numeric values for statistical visualization
datos = [12, 15, 18, 22, 25, 28, 30, 32, 35, 38, 40, 22, 24, 26, 29]

# Create two side-by-side subplots sharing one figure; unpack axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Histogram
# bins=6 divides the data range into 6 equal intervals
ax1.hist(datos, bins=6, color="coral", edgecolor="white")
# X-axis label (Spanish display text preserved)
ax1.set_xlabel("Valor")
# Y-axis label: frequency count per bin
ax1.set_ylabel("Frecuencia")
ax1.set_title("Histograma")
# Light grid lines for readability (alpha < 1 = semi-transparent)
ax1.grid(True, alpha=0.3)

# Boxplot
# patch_artist=True fills box with color; shows median, quartiles, outliers
ax2.boxplot(datos, patch_artist=True)
ax2.set_ylabel("Valor")
ax2.set_title("Diagrama de caja")
# Only horizontal grid lines for easier value reading
ax2.grid(True, alpha=0.3, axis="y")

# Super title for the entire figure (above both subplots)
plt.suptitle("Análisis estadístico de una variable")
# Auto-adjust spacing so suptitle and labels don't overlap
plt.tight_layout()
plt.show()
