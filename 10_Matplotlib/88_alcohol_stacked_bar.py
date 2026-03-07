# -------------------------------------------------
# File Name: 35_alcohol_stacked_bar.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Stacked Bar: Beverage Types per Country.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "alcohol_consumption.csv"
df = pd.read_csv(csv_path)

df_top = df.sort_values("total_litres", ascending=False)
x_pos = np.arange(len(df_top))

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x_pos, df_top["beer_servings"], label="Beer",
       color="#F0A830", edgecolor="black", linewidth=0.3)
ax.bar(x_pos, df_top["spirit_servings"], bottom=df_top["beer_servings"],
       label="Spirits", color="#45B7D1", edgecolor="black", linewidth=0.3)
ax.bar(x_pos, df_top["wine_servings"],
       bottom=df_top["beer_servings"] + df_top["spirit_servings"],
       label="Wine", color="#8B0000", edgecolor="black", linewidth=0.3)

ax.set_xticks(x_pos)
ax.set_xticklabels(df_top["country"], rotation=45, ha="right", fontsize=9)
ax.set_title("Beverage Servings by Country (Stacked)", fontsize=14, fontweight="bold")
ax.set_ylabel("Servings")
ax.legend(fontsize=10)
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
