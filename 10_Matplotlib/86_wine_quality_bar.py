# -------------------------------------------------
# File Name: 33_wine_quality_bar.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Grouped Bar: Avg Properties by Quality Rating.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "wine_quality.csv"
df = pd.read_csv(csv_path)

quality_avg = df.groupby("quality")[["alcohol", "fixed_acidity", "pH"]].mean()

x_pos = np.arange(len(quality_avg))
width = 0.25

fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(x_pos - width, quality_avg["alcohol"], width,
       label="Alcohol (%)", color="#4ECDC4", edgecolor="black", linewidth=0.5)
ax.bar(x_pos, quality_avg["fixed_acidity"], width,
       label="Fixed Acidity", color="#FF6B6B", edgecolor="black", linewidth=0.5)
ax.bar(x_pos + width, quality_avg["pH"], width,
       label="pH", color="#45B7D1", edgecolor="black", linewidth=0.5)

ax.set_xticks(x_pos)
ax.set_xticklabels([f"Q{int(q)}" for q in quality_avg.index])
ax.set_title("Average Wine Properties by Quality Rating", fontsize=14, fontweight="bold")
ax.set_ylabel("Value")
ax.legend()
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
