# -------------------------------------------------
# File Name: 50_auto_hp_scatter.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Scatter plot of horsepower vs MPG by cylinders.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "auto_mpg_cars.csv"
df = pd.read_csv(csv_path)

plt.figure(figsize=(9, 6))
cyl_colors = {4: "#4ECDC4", 6: "#FFEAA7", 8: "#FF6B6B"}

for cyl, color in cyl_colors.items():
    subset = df[df["cylinders"] == cyl]
    plt.scatter(subset["horsepower"], subset["mpg"],
                label=f"{cyl} cyl", color=color, s=80,
                edgecolors="black", linewidth=0.4, alpha=0.8)

z = np.polyfit(df["horsepower"].dropna(), df["mpg"].dropna(), 2)
p = np.poly1d(z)
x_smooth = np.linspace(df["horsepower"].min(), df["horsepower"].max(), 100)
plt.plot(x_smooth, p(x_smooth), "k--", linewidth=1.5, alpha=0.6, label="Trend (quadratic)")

plt.title("Horsepower vs Fuel Efficiency", fontsize=14, fontweight="bold")
plt.xlabel("Horsepower")
plt.ylabel("Miles per Gallon (MPG)")
plt.legend(title="Cylinders", fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
