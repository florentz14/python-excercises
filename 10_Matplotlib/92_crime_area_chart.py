# -------------------------------------------------
# File Name: 39_crime_area_chart.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Stacked Area: Crime Categories Over Time.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "us_crime_rates.csv"
df = pd.read_csv(csv_path)

plt.figure(figsize=(10, 6))
plt.fill_between(df["Year"], df["Murder"], alpha=0.7, color="#FF6B6B", label="Murder")
plt.fill_between(df["Year"], df["Murder"], df["Murder"] + df["Robbery"],
                 alpha=0.7, color="#4ECDC4", label="Robbery")
plt.fill_between(df["Year"], df["Murder"] + df["Robbery"],
                 df["Murder"] + df["Robbery"] + df["Burglary"],
                 alpha=0.7, color="#45B7D1", label="Burglary")

plt.title("Crime Categories Over Time (Stacked Area)", fontsize=14, fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Number of Crimes")
plt.legend(loc="upper right", fontsize=10)
plt.grid(True, alpha=0.3)
plt.xticks(df["Year"], rotation=45)
plt.tight_layout()
plt.show()
