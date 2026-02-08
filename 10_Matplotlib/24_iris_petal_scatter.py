# -------------------------------------------------
# File Name: 24_iris_petal_scatter.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Scatter Plot — Petal Length vs Width by Species.
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

plt.figure(figsize=(8, 6))
for species, color in species_colors.items():
    subset = df[df["species"] == species]
    plt.scatter(subset["petal_length"], subset["petal_width"],
                label=species.capitalize(), color=color, s=70,
                edgecolors="black", linewidth=0.4, alpha=0.8)

plt.title("Petal Length vs Width by Species", fontsize=14, fontweight="bold")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.legend(title="Species", fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
