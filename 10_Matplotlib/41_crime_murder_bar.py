# -------------------------------------------------
# File Name: 41_crime_murder_bar.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Bar: Murder Count per Year with Trend Line.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "us_crime_rates.csv"
df = pd.read_csv(csv_path)

plt.figure(figsize=(10, 5))
colors = plt.cm.Reds(np.linspace(0.3, 0.9, len(df)))

plt.bar(df["Year"].astype(str), df["Murder"], color=colors,
        edgecolor="black", linewidth=0.5)

z = np.polyfit(df["Year"], df["Murder"], 2)
p = np.poly1d(z)
x_smooth = np.linspace(df["Year"].min(), df["Year"].max(), 100)
plt.plot(x_smooth, p(x_smooth), "k--", linewidth=2, label="Trend (quadratic)")

plt.title("Murder Count per Year with Trend", fontsize=14, fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Murder Count")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
