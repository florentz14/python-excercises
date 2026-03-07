# -------------------------------------------------
# File Name: 45_students_alcohol_bar.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Bar chart of average final grade by weekend alcohol level.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "students_alcohol.csv"
df = pd.read_csv(csv_path)

# Group by weekend alcohol consumption (Walc: 1=very low to 5=very high)
walc_avg = df.groupby("Walc")["G3"].mean()

plt.figure(figsize=(7, 5))
colors = plt.cm.RdYlGn_r(np.linspace(0.2, 0.9, len(walc_avg)))
bars = plt.bar(walc_avg.index.astype(str), walc_avg.values, color=colors,
               edgecolor="black", linewidth=0.8)

for bar, val in zip(bars, walc_avg.values):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
             f"{val:.1f}", ha="center", fontweight="bold", fontsize=10)

plt.title("Avg Final Grade by Weekend Alcohol Level", fontsize=14, fontweight="bold")
plt.xlabel("Weekend Alcohol Consumption (1=very low, 5=very high)")
plt.ylabel("Average Final Grade (G3)")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
