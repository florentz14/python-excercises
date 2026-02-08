# -------------------------------------------------
# File Name: 20_players_top_scorers.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Horizontal Bar — Top 10 Players by Score.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

# Load CSV from the 09_Pandas folder
csv_path = Path(__file__).parent.parent / "09_Pandas" / "players.csv"
df = pd.read_csv(csv_path)

# Sort by score descending, take top 10
top_10 = df.dropna(subset=["score"]).nlargest(10, "score")

plt.figure(figsize=(8, 5))
colors = plt.cm.RdYlGn(np.linspace(0.3, 0.9, len(top_10)))  # Red-to-green gradient
plt.barh(top_10["name"], top_10["score"], color=colors, edgecolor="black", linewidth=0.5)

# Add score labels at end of each bar
for i, (val, name) in enumerate(zip(top_10["score"], top_10["name"])):
    plt.text(val + 0.2, i, f"{val:.1f}", va="center", fontsize=9, fontweight="bold")

plt.title("Top 10 Players by Score", fontsize=14, fontweight="bold")
plt.xlabel("Score")
plt.gca().invert_yaxis()  # Highest score at the top
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.show()
