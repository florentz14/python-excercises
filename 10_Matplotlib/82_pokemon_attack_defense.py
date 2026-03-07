# -------------------------------------------------
# File Name: 29_pokemon_attack_defense.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Grouped Bar — Attack vs Defense per Pokémon.
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

x_pos = np.arange(len(df))  # Numeric positions for each Pokémon
width = 0.35  # Bar width

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(x_pos - width / 2, df["attack"], width,
       label="Attack", color="#FF6B6B", edgecolor="black", linewidth=0.5)
ax.bar(x_pos + width / 2, df["defense"], width,
       label="Defense", color="#4ECDC4", edgecolor="black", linewidth=0.5)

ax.set_xticks(x_pos)
ax.set_xticklabels(df["name"], rotation=45, ha="right", fontsize=9)  # Rotate for readability
ax.set_title("Attack vs Defense by Pokémon", fontsize=14, fontweight="bold")
ax.set_ylabel("Stat Value")
ax.legend()
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
