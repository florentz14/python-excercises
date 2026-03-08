# -------------------------------------------------
# File Name: 117_titanic_plots.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Titanic: pie, histogram, bar charts (survival, class).
# -------------------------------------------------

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA = Path(__file__).parent.parent / "09_Pandas" / "data"
OUTPUT = Path(__file__).parent / "output"
df = pd.read_csv(DATA / "titanic.csv")

OUTPUT.mkdir(exist_ok=True)

# 1. Pie: dead vs survived
fig1, ax1 = plt.subplots(figsize=(6, 6))
counts = df["Survived"].value_counts()
labels = ["Dead", "Survived"]
ax1.pie(counts.values, labels=labels, autopct="%1.1f%%", startangle=90)
ax1.set_title("Dead vs Survived", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig(OUTPUT / "titanic_pie_survival.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: titanic_pie_survival.png")

# 2. Histogram: ages
fig2, ax2 = plt.subplots(figsize=(7, 5))
ax2.hist(df["Age"].dropna(), bins=20, color="steelblue", edgecolor="black")
ax2.set_title("Age Distribution", fontsize=14, fontweight="bold")
ax2.set_xlabel("Age")
ax2.set_ylabel("Count")
plt.tight_layout()
plt.savefig(OUTPUT / "titanic_hist_ages.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: titanic_hist_ages.png")

# 3. Bar: people per class
fig3, ax3 = plt.subplots(figsize=(6, 5))
class_counts = df["Pclass"].value_counts().sort_index()
ax3.bar(class_counts.index.astype(str), class_counts.values, color="coral", edgecolor="black")
ax3.set_title("People per Class", fontsize=14, fontweight="bold")
ax3.set_xlabel("Class")
ax3.set_ylabel("Count")
plt.tight_layout()
plt.savefig(OUTPUT / "titanic_bar_class.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: titanic_bar_class.png")

# 4. Bar: dead/survived per class (grouped)
fig4, ax4 = plt.subplots(figsize=(7, 5))
cross = pd.crosstab(df["Pclass"], df["Survived"])
x = range(len(cross.index))
w = 0.35
ax4.bar([i - w/2 for i in x], cross[0], w, label="Dead", color="coral")
ax4.bar([i + w/2 for i in x], cross[1], w, label="Survived", color="steelblue")
ax4.set_xticks(x)
ax4.set_xticklabels(cross.index.astype(str))
ax4.set_title("Dead and Survived per Class", fontsize=14, fontweight="bold")
ax4.set_xlabel("Class")
ax4.set_ylabel("Count")
ax4.legend()
plt.tight_layout()
plt.savefig(OUTPUT / "titanic_bar_class_survival.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: titanic_bar_class_survival.png")

# 5. Bar: dead/survived accumulated per class (stacked)
fig5, ax5 = plt.subplots(figsize=(7, 5))
ax5.bar(cross.index.astype(str), cross[0], label="Dead", color="coral")
ax5.bar(cross.index.astype(str), cross[1], bottom=cross[0], label="Survived", color="steelblue")
ax5.set_title("Dead and Survived (Stacked) per Class", fontsize=14, fontweight="bold")
ax5.set_xlabel("Class")
ax5.set_ylabel("Count")
ax5.legend()
plt.tight_layout()
plt.savefig(OUTPUT / "titanic_bar_stacked.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: titanic_bar_stacked.png")

print("\nAll 5 Titanic charts saved.")
