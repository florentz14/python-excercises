# -------------------------------------------------
# File Name: 36_alcohol_continent_pie.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Pie: Average Consumption by Continent.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "alcohol_consumption.csv"
df = pd.read_csv(csv_path)

continent_avg = df.groupby("continent")["total_litres"].mean().sort_values(ascending=False)
pie_colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"]

plt.figure(figsize=(7, 7))
wedges, texts, autotexts = plt.pie(
    continent_avg.values, labels=continent_avg.index, autopct="%1.1f%%",
    colors=pie_colors[:len(continent_avg)], startangle=140,
    explode=[0.05] * len(continent_avg), textprops={"fontsize": 11})

for at in autotexts:
    at.set_fontweight("bold")

plt.title("Avg Alcohol Consumption by Continent", fontsize=14, fontweight="bold", pad=20)
plt.axis("equal")
plt.tight_layout()
plt.show()
