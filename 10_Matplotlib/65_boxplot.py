# -------------------------------------------------
# File Name: 12_boxplot.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Box Plots (Boxplot).
#              Display median, quartiles, and outliers using
#              plt.boxplot(). Compare distributions across
#              groups with patch_artist styling.
# -------------------------------------------------

"""
Matplotlib - Example 5: Box Plot (boxplot, statistical chart)
===============================================================
Topic: Matplotlib (10_Matplotlib)
Description: plt.boxplot() displays median, quartiles, and outliers.
Useful for comparing distributions and detecting outliers.
"""

import matplotlib.pyplot as plt
# matplotlib.pyplot provides all the plotting functions

# Sample data: three groups (A, B, C) — each list is a distribution
datos = [
    [22, 25, 28, 30, 32, 35, 38],
    [18, 24, 27, 29, 31, 36, 42],
    [20, 23, 26, 28, 30, 33, 45],
]

# A boxplot shows the median (center line), quartiles (box edges),
# whiskers (range), and outliers (dots beyond whiskers)
plt.figure(figsize=(6, 4))
# patch_artist=True fills the box with color (default is outline only)
cajas = plt.boxplot(datos, labels=["Grupo A", "Grupo B", "Grupo C"], patch_artist=True)  # Boxes variable
# Iterate over box patches to customize each box's fill color
for caja in cajas["boxes"]:
    # Set the interior color of each box
    caja.set_facecolor("lightblue")
# Y-axis label (Spanish "Value" kept as display text)
plt.ylabel("Valor")
plt.title("Diagrama de caja (boxplot)")
# Show horizontal grid lines only for easier value comparison
plt.grid(True, alpha=0.3, axis="y")
# Adjust padding so labels don't get cut off
plt.tight_layout()
plt.show()
