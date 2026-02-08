# -------------------------------------------------
# File Name: 31_wine_type_box.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Box Plot: Alcohol and pH by Wine Type.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "wine_quality.csv"
df = pd.read_csv(csv_path)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("Wine Properties by Type (Red vs White)", fontsize=14, fontweight="bold")

red_alc = df[df["wine_type"] == "red"]["alcohol"].dropna().values
white_alc = df[df["wine_type"] == "white"]["alcohol"].dropna().values

bp1 = axes[0].boxplot([red_alc, white_alc], labels=["Red", "White"],
                       patch_artist=True, medianprops=dict(color="black", linewidth=2))
bp1["boxes"][0].set_facecolor("#FF9999")
bp1["boxes"][1].set_facecolor("#FFFFAA")
axes[0].set_title("Alcohol Content")
axes[0].set_ylabel("Alcohol (%)")
axes[0].grid(axis="y", alpha=0.3)

red_ph = df[df["wine_type"] == "red"]["pH"].dropna().values
white_ph = df[df["wine_type"] == "white"]["pH"].dropna().values

bp2 = axes[1].boxplot([red_ph, white_ph], labels=["Red", "White"],
                       patch_artist=True, medianprops=dict(color="black", linewidth=2))
bp2["boxes"][0].set_facecolor("#FF9999")
bp2["boxes"][1].set_facecolor("#FFFFAA")
axes[1].set_title("pH Level")
axes[1].set_ylabel("pH")
axes[1].grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()
