# -------------------------------------------------
# File Name: 40_crime_type_panels.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Subplots: Individual Crime Type Trends (2x2).
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "us_crime_rates.csv"
df = pd.read_csv(csv_path)

crime_types = [("Murder", "#FF6B6B"), ("Robbery", "#4ECDC4"),
               ("Burglary", "#45B7D1"), ("Violent", "#96CEB4")]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Individual Crime Type Trends", fontsize=14, fontweight="bold")

for ax, (crime, color) in zip(axes.flat, crime_types):
    ax.plot(df["Year"], df[crime], "-o", color=color, linewidth=2, markersize=5)
    ax.fill_between(df["Year"], df[crime], alpha=0.2, color=color)
    ax.set_title(crime, fontsize=12)
    ax.set_xlabel("Year")
    ax.set_ylabel("Count")
    ax.grid(True, alpha=0.3)
    ax.tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.show()
