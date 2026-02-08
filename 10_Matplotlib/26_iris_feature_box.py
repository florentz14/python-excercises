# -------------------------------------------------
# File Name: 26_iris_feature_box.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Box Plots — All Features by Species (side by side).
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

# Load CSV from the 09_Pandas folder
csv_path = Path(__file__).parent.parent / "09_Pandas" / "iris.csv"
df = pd.read_csv(csv_path).dropna()  # Drop rows with missing values for clean plots

# Map species to colors for consistent coloring
species_colors = {"setosa": "#FF6B6B", "versicolor": "#4ECDC4", "virginica": "#45B7D1"}

features = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
species_list = list(species_colors.keys())

fig, axes = plt.subplots(1, 4, figsize=(14, 5))
fig.suptitle("Feature Box Plots by Species", fontsize=14, fontweight="bold")

for ax, feature in zip(axes, features):
    # Create a list of arrays — one per species — for the boxplot
    data_per_species = [df[df["species"] == sp][feature].values for sp in species_list]

    bp = ax.boxplot(data_per_species, labels=[s.capitalize() for s in species_list],
                    patch_artist=True,  # Fill boxes with color
                    medianprops=dict(color="black", linewidth=1.5))

    # Color each box by species
    for patch, sp in zip(bp["boxes"], species_list):
        patch.set_facecolor(species_colors[sp])

    ax.set_title(feature.replace("_", " ").title(), fontsize=10)
    ax.set_ylabel("cm")
    ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()
