# -------------------------------------------------
# File Name: 44_students_school_box.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Box plot of grades by school (GP vs MS).
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "students_alcohol.csv"
df = pd.read_csv(csv_path)

fig, axes = plt.subplots(1, 3, figsize=(14, 5))
fig.suptitle("Grade Distribution by School", fontsize=14, fontweight="bold")

grade_cols = ["G1", "G2", "G3"]  # Period 1, 2, and Final grades
school_colors = {"GP": "#4ECDC4", "MS": "#FF6B6B"}

for ax, grade in zip(axes, grade_cols):
    schools = df["school"].unique()
    data = [df[df["school"] == s][grade].values for s in schools]

    bp = ax.boxplot(data, labels=schools, patch_artist=True,
                    medianprops=dict(color="black", linewidth=2))

    for patch, school in zip(bp["boxes"], schools):
        patch.set_facecolor(school_colors[school])

    ax.set_title(f"{grade} (Period {'Final' if grade == 'G3' else grade[1]})")
    ax.set_ylabel("Grade")
    ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()
