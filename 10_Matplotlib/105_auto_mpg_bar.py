# -------------------------------------------------
# File Name: 52_auto_mpg_bar.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Bar chart of average MPG by cylinder count.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "auto_mpg_cars.csv"
df = pd.read_csv(csv_path)

cyl_colors = {4: "#4ECDC4", 6: "#FFEAA7", 8: "#FF6B6B"}
avg_mpg = df.groupby("cylinders")["mpg"].mean()

plt.figure(figsize=(7, 5))
bar_colors = [cyl_colors.get(c, "#999999") for c in avg_mpg.index]
bars = plt.bar(avg_mpg.index.astype(str), avg_mpg.values, color=bar_colors,
               edgecolor="black", linewidth=0.8)

for bar, val in zip(bars, avg_mpg.values):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
             f"{val:.1f}", ha="center", fontweight="bold", fontsize=11)

plt.title("Average MPG by Cylinder Count", fontsize=14, fontweight="bold")
plt.xlabel("Number of Cylinders")
plt.ylabel("Average MPG")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
