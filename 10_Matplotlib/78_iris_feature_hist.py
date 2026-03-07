# -------------------------------------------------
# File Name: 25_iris_feature_hist.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Histograms — Feature Distributions by Species (2x2 grid).
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
fig, axes = plt.subplots(2, 2, figsize=(10, 8))  # 2x2 grid for 4 features
fig.suptitle("Feature Distributions by Species", fontsize=14, fontweight="bold")

for ax, feature in zip(axes.flat, features):
    for species, color in species_colors.items():
        subset = df[df["species"] == species][feature]
        # alpha=0.5 makes histograms semi-transparent so they can overlap visibly
        ax.hist(subset, bins=10, alpha=0.5, color=color, edgecolor="black",
                label=species.capitalize(), linewidth=0.5)
    ax.set_title(feature.replace("_", " ").title(), fontsize=11)  # Format column name as title
    ax.set_xlabel("cm")
    ax.set_ylabel("Count")
    ax.legend(fontsize=8)
    ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()
