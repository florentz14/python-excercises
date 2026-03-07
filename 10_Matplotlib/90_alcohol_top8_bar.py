# -------------------------------------------------
# File Name: 37_alcohol_top8_bar.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Grouped Bar: Beer vs Wine vs Spirits (Top 8).
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "alcohol_consumption.csv"
df = pd.read_csv(csv_path)

top_8 = df.nlargest(8, "total_litres")
x_pos = np.arange(len(top_8))
width = 0.25

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(x_pos - width, top_8["beer_servings"], width,
       label="Beer", color="#F0A830", edgecolor="black", linewidth=0.5)
ax.bar(x_pos, top_8["spirit_servings"], width,
       label="Spirits", color="#45B7D1", edgecolor="black", linewidth=0.5)
ax.bar(x_pos + width, top_8["wine_servings"], width,
       label="Wine", color="#8B0000", edgecolor="black", linewidth=0.5)

ax.set_xticks(x_pos)
ax.set_xticklabels(top_8["country"], rotation=30, ha="right")
ax.set_title("Beverage Breakdown — Top 8 Countries", fontsize=14, fontweight="bold")
ax.set_ylabel("Servings")
ax.legend()
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
