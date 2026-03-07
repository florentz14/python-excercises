# -------------------------------------------------
# File Name: 46_euro12_goals_bar.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Horizontal bar chart of goals scored by team (Euro 2012).
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "euro12.csv"
df = pd.read_csv(csv_path)

df_sorted = df.sort_values("Goals", ascending=True)

plt.figure(figsize=(8, 5))
colors = plt.cm.cool(np.linspace(0.2, 0.9, len(df_sorted)))
bars = plt.barh(df_sorted["Team"], df_sorted["Goals"], color=colors,
                edgecolor="black", linewidth=0.5)

for bar, val in zip(bars, df_sorted["Goals"]):
    plt.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height() / 2,
             str(int(val)), va="center", fontweight="bold", fontsize=10)

plt.title("Goals Scored by Team — Euro 2012", fontsize=14, fontweight="bold")
plt.xlabel("Goals")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.show()
