# -------------------------------------------------
# File Name: 30_titanic_viz.py
# Author: Florentino Báez
# Date: Pandas
# Description: Visualize Titanic Passenger Data. Create survival rate charts,
#              age distribution histograms, class comparisons, and gender
#              analysis using matplotlib.
# -------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Create Titanic DataFrame: PassengerId, Survived, Pclass, Name, Sex, Age, Fare, Embarked
# At least 20 rows
csv_path = Path(__file__).parent / "titanic.csv"
df = pd.read_csv(csv_path)

print("Titanic data (sample):")
print(df.head())

# --- Bar chart: survival rate by class ---
survival_by_class = df.groupby("Pclass")["Survived"].mean() * 100

plt.figure(figsize=(7, 5))
plt.bar(survival_by_class.index.astype(str), survival_by_class.values, color=["gold", "silver", "chocolate"])
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Class")
plt.ylabel("Survival Rate (%)")
plt.tight_layout()
plt.savefig("titanic_survival_by_class.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Histogram: age distribution of passengers ---
plt.figure(figsize=(7, 5))
plt.hist(df["Age"].dropna(), bins=10, color="steelblue", edgecolor="black")
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("titanic_age_histogram.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Grouped bar chart: survival by gender ---
survival_by_sex = df.groupby("Sex")["Survived"].agg(["sum", "count"])
survival_by_sex["survived_pct"] = survival_by_sex["sum"] / survival_by_sex["count"] * 100
survival_by_sex["died_pct"] = 100 - survival_by_sex["survived_pct"]

x = np.arange(len(survival_by_sex))
width = 0.35
fig, ax = plt.subplots(figsize=(7, 5))
ax.bar(x - width/2, survival_by_sex["survived_pct"], width, label="Survived", color="green")
ax.bar(x + width/2, survival_by_sex["died_pct"], width, label="Died", color="red")
ax.set_xticks(x)
ax.set_xticklabels(survival_by_sex.index)
ax.set_ylabel("Percentage")
ax.set_title("Survival by Gender")
ax.legend()
plt.tight_layout()
plt.savefig("titanic_survival_by_gender.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Pie chart: passenger class distribution ---
class_counts = df["Pclass"].value_counts().sort_index()

plt.figure(figsize=(6, 6))
plt.pie(class_counts.values, labels=[f"Class {c}" for c in class_counts.index], autopct="%1.1f%%", startangle=90)
plt.title("Passenger Class Distribution")
plt.tight_layout()
plt.savefig("titanic_pie_class.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Box plot: fare distribution by class ---
df_box = df[["Pclass", "Fare"]].copy()
df_box["Pclass"] = df_box["Pclass"].astype(str)

plt.figure(figsize=(7, 5))
df.boxplot(column="Fare", by="Pclass", ax=plt.gca())
plt.suptitle("")
plt.title("Fare Distribution by Class")
plt.xlabel("Class")
plt.ylabel("Fare")
plt.tight_layout()
plt.savefig("titanic_fare_boxplot.png", dpi=100, bbox_inches="tight")
plt.show()

print("Plots saved: titanic_survival_by_class.png, titanic_age_histogram.png, titanic_survival_by_gender.png, titanic_pie_class.png, titanic_fare_boxplot.png")
