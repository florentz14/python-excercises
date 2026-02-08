# -------------------------------------------------
# File Name: 22_players_position_pie.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Pie Chart — Player Distribution by Position.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

# Load CSV from the 09_Pandas folder
csv_path = Path(__file__).parent.parent / "09_Pandas" / "players.csv"
df = pd.read_csv(csv_path)

pos_counts = df["position"].value_counts()  # Count players per position

plt.figure(figsize=(7, 7))
explode = [0.05] * len(pos_counts)  # Slight gap between all slices
plt.pie(pos_counts.values, labels=pos_counts.index, autopct="%1.0f%%",
        colors=["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"],
        explode=explode, startangle=90, shadow=True,
        textprops={"fontsize": 11, "fontweight": "bold"})

plt.title("Player Distribution by Position", fontsize=14, fontweight="bold", pad=20)
plt.axis("equal")
plt.tight_layout()
plt.show()
