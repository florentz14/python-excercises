# -------------------------------------------------
# File Name: 51_auto_mpg_hist.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Histograms of MPG distribution by cylinder count (1x3).
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "auto_mpg_cars.csv"
df = pd.read_csv(csv_path)

cyl_colors = {4: "#4ECDC4", 6: "#FFEAA7", 8: "#FF6B6B"}

fig, axes = plt.subplots(1, 3, figsize=(14, 4))
fig.suptitle("MPG Distribution by Cylinder Count", fontsize=14, fontweight="bold")

for ax, (cyl, color) in zip(axes, cyl_colors.items()):
    subset = df[df["cylinders"] == cyl]["mpg"]
    ax.hist(subset, bins=8, color=color, edgecolor="black", alpha=0.8)
    ax.set_title(f"{cyl} Cylinders (n={len(subset)})")
    ax.set_xlabel("MPG")
    ax.set_ylabel("Count")
    ax.axvline(subset.mean(), color="red", linestyle="--", linewidth=1.5,
               label=f"Mean: {subset.mean():.1f}")
    ax.legend(fontsize=9)
    ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()
