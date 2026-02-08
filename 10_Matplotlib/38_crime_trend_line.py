# -------------------------------------------------
# File Name: 38_crime_trend_line.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Line Chart: Violent vs Property Crime Over Time.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "us_crime_rates.csv"
df = pd.read_csv(csv_path)

plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["Violent"], "r-o", linewidth=2, markersize=6, label="Violent Crime")
plt.plot(df["Year"], df["Property"], "b-s", linewidth=2, markersize=6, label="Property Crime")

plt.title("US Crime Trends: Violent vs Property", fontsize=14, fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Number of Crimes")
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.xticks(df["Year"], rotation=45)
plt.tight_layout()
plt.show()
