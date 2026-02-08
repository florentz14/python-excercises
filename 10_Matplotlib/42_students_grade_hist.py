# -------------------------------------------------
# File Name: 42_students_grade_hist.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Histogram of distribution of final grades (G3).
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

csv_path = Path(__file__).parent.parent / "09_Pandas" / "students_alcohol.csv"
df = pd.read_csv(csv_path)

plt.figure(figsize=(8, 5))
plt.hist(df["G3"], bins=10, color="steelblue", edgecolor="black", alpha=0.8)

mean_g3 = df["G3"].mean()
plt.axvline(mean_g3, color="red", linestyle="--", linewidth=2, label=f"Mean: {mean_g3:.1f}")

plt.title("Distribution of Final Grades (G3)", fontsize=14, fontweight="bold")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")
plt.legend(fontsize=11)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
