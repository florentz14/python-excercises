# -------------------------------------------------
# File Name: 48_euro12_accuracy_scatter.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Scatter plot of shooting accuracy vs goals (color=passes).
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "euro12.csv"
df = pd.read_csv(csv_path)

plt.figure(figsize=(8, 6))
plt.scatter(df["Shooting Accuracy"], df["Goals"], s=150,
            c=df["Passes"], cmap="YlOrRd",
            edgecolors="black", linewidth=0.8, zorder=5)

for _, row in df.iterrows():
    plt.annotate(row["Team"],
                 xy=(row["Shooting Accuracy"], row["Goals"]),
                 xytext=(5, 5), textcoords="offset points",
                 fontsize=9, fontweight="bold")

plt.colorbar(label="Total Passes")
plt.title("Shooting Accuracy vs Goals (color = Passes)", fontsize=14, fontweight="bold")
plt.xlabel("Shooting Accuracy (%)")
plt.ylabel("Goals Scored")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
