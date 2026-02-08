# -------------------------------------------------
# File Name: 30_visualization_titanic.py
# Author: Florentino Báez
# Date: Pandas
# Description: Visualize Titanic Passenger Data. Create survival rate charts,
#              age distribution histograms, class comparisons, and gender
#              analysis using matplotlib.
# -------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create Titanic DataFrame: PassengerId, Survived, Pclass, Name, Sex, Age, Fare, Embarked
# At least 20 rows
data = {
    "PassengerId": range(1, 26),
    "Survived": [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    "Pclass": [3, 1, 3, 1, 3, 2, 3, 2, 3, 1, 2, 3, 3, 1, 2, 1, 3, 2, 3, 1, 2, 2, 1, 3, 2],
    "Name": [f"Passenger_{i}" for i in range(1, 26)],
    "Sex": ["male", "female", "female", "female", "male", "male", "male", "female", "female", "female",
            "male", "male", "female", "male", "female", "female", "male", "female", "male", "female",
            "male", "female", "female", "male", "female"],
    "Age": [22, 38, 26, 35, 28, 45, 30, 25, 19, 40, 32, 28, 22, 50, 36, 24, 29, 18, 34, 42, 27, 31, 21, 33, 17],
    "Fare": [7.25, 71.28, 7.92, 53.1, 8.05, 13.5, 8.46, 21.07, 7.13, 30.0, 13.0, 8.03, 7.22, 26.55, 12.47,
             27.72, 9.68, 11.34, 7.89, 26.0, 10.5, 15.75, 31.0, 7.75, 14.45],
    "Embarked": ["S", "C", "S", "S", "S", "S", "Q", "S", "S", "C", "S", "S", "S", "S", "S",
                 "C", "S", "S", "Q", "S", "S", "S", "C", "S", "S"]
}

df = pd.DataFrame(data)

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
