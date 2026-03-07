# -------------------------------------------------
# File Name: 28_pokemon_total_stats.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Horizontal Bar — Total Stats per Pokémon (sorted).
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

# Load CSV from the 09_Pandas folder
csv_path = Path(__file__).parent.parent / "09_Pandas" / "pokemon.csv"
df = pd.read_csv(csv_path)

# The stat columns we'll plot
stat_cols = ["hp", "attack", "defense", "speed"]

# Calculate the sum of all stat columns for each Pokémon
df["total_stats"] = df[stat_cols].sum(axis=1)  # axis=1 sums across columns
df_sorted = df.sort_values("total_stats", ascending=True)  # Ascending for horizontal bar

plt.figure(figsize=(8, 7))
colors = plt.cm.plasma(np.linspace(0.2, 0.9, len(df_sorted)))  # Gradient from plasma colormap
plt.barh(df_sorted["name"], df_sorted["total_stats"], color=colors,
         edgecolor="black", linewidth=0.5)

# Add value labels at the end of each bar
for i, (val, name) in enumerate(zip(df_sorted["total_stats"], df_sorted["name"])):
    plt.text(val + 3, i, str(int(val)), va="center", fontsize=9)

plt.title("Total Stats by Pokémon", fontsize=14, fontweight="bold")
plt.xlabel("Total (HP + Attack + Defense + Speed)")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.show()
