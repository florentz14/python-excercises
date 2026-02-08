# -------------------------------------------------
# File Name: 30_wine_alcohol_hist.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Histogram: Alcohol Distribution by Wine Type.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "wine_quality.csv"
df = pd.read_csv(csv_path)

plt.figure(figsize=(8, 5))
red = df[df["wine_type"] == "red"]["alcohol"]
white = df[df["wine_type"] == "white"]["alcohol"]

plt.hist(red, bins=8, alpha=0.6, color="#8B0000", edgecolor="black",
         label=f"Red (n={len(red)})", linewidth=0.5)
plt.hist(white, bins=8, alpha=0.6, color="#FFD700", edgecolor="black",
         label=f"White (n={len(white)})", linewidth=0.5)

plt.title("Alcohol Content Distribution by Wine Type", fontsize=14, fontweight="bold")
plt.xlabel("Alcohol (%)")
plt.ylabel("Number of Wines")
plt.legend(fontsize=11)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
