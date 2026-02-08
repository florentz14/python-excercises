# -------------------------------------------------
# File Name: 19_players_goals_scatter.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Scatter Plot — Goals vs Score Colored by Position.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

# Load CSV from the 09_Pandas folder
csv_path = Path(__file__).parent.parent / "09_Pandas" / "players.csv"
df = pd.read_csv(csv_path)

# Drop rows with missing score or goals for clean scatter
clean = df.dropna(subset=["score", "goals"])

# Map each position to a color
positions = clean["position"].unique()
color_map = {pos: c for pos, c in zip(positions, plt.cm.tab10.colors)}  # tab10 gives distinct colors

plt.figure(figsize=(8, 6))
for pos in positions:
    mask = clean["position"] == pos  # Boolean mask for this position
    plt.scatter(clean.loc[mask, "goals"], clean.loc[mask, "score"],
                label=pos, color=color_map[pos], s=100, edgecolors="black",
                linewidth=0.5, alpha=0.8)

plt.title("Goals vs Score by Position", fontsize=14, fontweight="bold")
plt.xlabel("Goals Scored")
plt.ylabel("Player Score")
plt.legend(title="Position", fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
