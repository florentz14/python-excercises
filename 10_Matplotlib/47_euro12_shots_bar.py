# -------------------------------------------------
# File Name: 47_euro12_shots_bar.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Grouped bar chart of shots on vs off target (Euro 2012).
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "euro12.csv"
df = pd.read_csv(csv_path)

x_pos = np.arange(len(df))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(x_pos - width / 2, df["Shots on target"], width,
       label="On Target", color="#4ECDC4", edgecolor="black", linewidth=0.5)
ax.bar(x_pos + width / 2, df["Shots off target"], width,
       label="Off Target", color="#FF6B6B", edgecolor="black", linewidth=0.5)

ax.set_xticks(x_pos)
ax.set_xticklabels(df["Team"], rotation=30, ha="right")
ax.set_title("Shots On vs Off Target — Euro 2012", fontsize=14, fontweight="bold")
ax.set_ylabel("Number of Shots")
ax.legend(fontsize=10)
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
