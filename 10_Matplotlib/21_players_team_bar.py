# -------------------------------------------------
# File Name: 21_players_team_bar.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Grouped Bar — Average Goals vs Attempts by Team.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

# Load CSV from the 09_Pandas folder
csv_path = Path(__file__).parent.parent / "09_Pandas" / "players.csv"
df = pd.read_csv(csv_path)

# Aggregate by team
team_stats = df.groupby("team")[["goals", "attempts"]].mean()

x_pos = np.arange(len(team_stats))  # Numeric positions for each team
width = 0.35  # Width of each bar group

fig, ax = plt.subplots(figsize=(10, 5))
# First bar group: average goals
bars1 = ax.bar(x_pos - width / 2, team_stats["goals"], width,
               label="Avg Goals", color="#4ECDC4", edgecolor="black", linewidth=0.5)
# Second bar group: average attempts
bars2 = ax.bar(x_pos + width / 2, team_stats["attempts"], width,
               label="Avg Attempts", color="#FF6B6B", edgecolor="black", linewidth=0.5)

ax.set_xticks(x_pos)
ax.set_xticklabels(team_stats.index, rotation=30, ha="right")
ax.set_title("Average Goals vs Attempts by Team", fontsize=14, fontweight="bold")
ax.set_ylabel("Count")
ax.legend()
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
