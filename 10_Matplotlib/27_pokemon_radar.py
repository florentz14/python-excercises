# -------------------------------------------------
# File Name: 27_pokemon_radar.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Radar Chart — Compare Stats of 4 Pokémon.
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

# Pick 4 Pokémon to compare (must exist in the CSV)
selected = ["Pikachu", "Charizard", "Bulbasaur", "Mewtwo"]
subset = df[df["name"].isin(selected)].set_index("name")

# Number of stat categories
N = len(stat_cols)
# Angles for each axis on the radar (one per stat, plus closing angle)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]  # Close the polygon by repeating the first angle

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))  # Polar axes for radar

colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#FFEAA7"]

for i, pokemon_name in enumerate(selected):
    if pokemon_name in subset.index:
        values = subset.loc[pokemon_name, stat_cols].values.tolist()
        values += values[:1]  # Close the polygon
        ax.plot(angles, values, "o-", linewidth=2, label=pokemon_name, color=colors[i])
        ax.fill(angles, values, alpha=0.15, color=colors[i])  # Transparent fill

# Set the stat names as labels around the radar
ax.set_xticks(angles[:-1])  # One tick per stat (exclude the closing duplicate)
ax.set_xticklabels([s.upper() for s in stat_cols], fontsize=11, fontweight="bold")

ax.set_title("Pokémon Stats Comparison (Radar)", fontsize=14, fontweight="bold", pad=20)
ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1), fontsize=10)
plt.tight_layout()
plt.show()
