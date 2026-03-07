# -------------------------------------------------
# File Name: 53_auto_bubble_chart.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Bubble chart of displacement vs MPG (size=horsepower).
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "auto_mpg_cars.csv"
df = pd.read_csv(csv_path)

plt.figure(figsize=(9, 6))
bubble_sizes = df["horsepower"] * 2

scatter = plt.scatter(df["displacement"], df["mpg"],
                      s=bubble_sizes, c=df["cylinders"],
                      cmap="coolwarm", alpha=0.6,
                      edgecolors="black", linewidth=0.3)

plt.colorbar(scatter, label="Cylinders")
plt.title("Displacement vs MPG (bubble size = Horsepower)", fontsize=14, fontweight="bold")
plt.xlabel("Displacement (cu. in.)")
plt.ylabel("Miles per Gallon (MPG)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
