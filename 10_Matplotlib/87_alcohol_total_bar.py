# -------------------------------------------------
# File Name: 34_alcohol_total_bar.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Horizontal Bar: Total Litres by Country.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "alcohol_consumption.csv"
df = pd.read_csv(csv_path)

df_sorted = df.sort_values("total_litres", ascending=True)

plt.figure(figsize=(8, 7))
colors = plt.cm.YlOrRd(np.linspace(0.2, 0.9, len(df_sorted)))
plt.barh(df_sorted["country"], df_sorted["total_litres"], color=colors,
         edgecolor="black", linewidth=0.5)

for i, (val, country) in enumerate(zip(df_sorted["total_litres"], df_sorted["country"])):
    plt.text(val + 0.1, i, f"{val:.1f}L", va="center", fontsize=8)

plt.title("Total Alcohol Consumption by Country", fontsize=14, fontweight="bold")
plt.xlabel("Total Litres of Pure Alcohol")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.show()
