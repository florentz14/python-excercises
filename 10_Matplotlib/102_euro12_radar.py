# -------------------------------------------------
# File Name: 49_euro12_radar.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Radar chart comparing top 3 teams (normalized).
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "euro12.csv"
df = pd.read_csv(csv_path)

top_3 = df.nlargest(3, "Goals")
stat_cols = ["Goals", "Shots on target", "Shooting Accuracy", "Pass Accuracy"]

N = len(stat_cols)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
colors = ["#FF6B6B", "#4ECDC4", "#45B7D1"]

for i, (_, row) in enumerate(top_3.iterrows()):
    values = []
    for col in stat_cols:
        col_min, col_max = df[col].min(), df[col].max()
        norm_val = (row[col] - col_min) / (col_max - col_min) if col_max > col_min else 0
        values.append(norm_val)
    values += values[:1]

    ax.plot(angles, values, "o-", linewidth=2, label=row["Team"], color=colors[i])
    ax.fill(angles, values, alpha=0.15, color=colors[i])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(stat_cols, fontsize=10, fontweight="bold")
ax.set_title("Top 3 Teams Comparison (Normalized)", fontsize=14, fontweight="bold", pad=20)
ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.show()
