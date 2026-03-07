# -------------------------------------------------
# File Name: 43_students_study_scatter.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Scatter plot of study time vs final grade by sex.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "students_alcohol.csv"
df = pd.read_csv(csv_path)

plt.figure(figsize=(8, 6))
for sex, color, marker in [("F", "#FF6B6B", "o"), ("M", "#4ECDC4", "s")]:
    subset = df[df["sex"] == sex]
    # Add jitter to studytime (integer values) to avoid overlapping dots
    jitter = np.random.uniform(-0.2, 0.2, len(subset))
    plt.scatter(subset["studytime"] + jitter, subset["G3"],
                label=f"{'Female' if sex == 'F' else 'Male'}",
                color=color, marker=marker, s=60, alpha=0.6,
                edgecolors="black", linewidth=0.3)

plt.title("Study Time vs Final Grade", fontsize=14, fontweight="bold")
plt.xlabel("Study Time (1=low, 4=high)")
plt.ylabel("Final Grade (G3)")
plt.xticks([1, 2, 3, 4])  # Study time is 1-4 scale
plt.legend(title="Sex", fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
