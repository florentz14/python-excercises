# -------------------------------------------------
# File Name: 32_wine_quality_scatter.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Scatter: Alcohol vs Quality by Wine Type.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "wine_quality.csv"
df = pd.read_csv(csv_path)

plt.figure(figsize=(8, 6))
for wine_type, color, marker in [("red", "#8B0000", "o"), ("white", "#DAA520", "s")]:
    subset = df[df["wine_type"] == wine_type]
    jitter = np.random.uniform(-0.15, 0.15, len(subset))
    plt.scatter(subset["alcohol"], subset["quality"] + jitter,
                label=wine_type.capitalize(), color=color, marker=marker,
                s=60, alpha=0.7, edgecolors="black", linewidth=0.3)

plt.title("Alcohol Content vs Quality Rating", fontsize=14, fontweight="bold")
plt.xlabel("Alcohol (%)")
plt.ylabel("Quality Rating (with jitter)")
plt.legend(title="Wine Type", fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
