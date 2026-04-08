# -------------------------------------------------
# File Name: 38_titanic_viz.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Survival charts, grouped bars, box plots for Titanic dataset.
# -------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Create Titanic DataFrame: PassengerId, Survived, Pclass, Name, Sex, Age, Fare, Embarked
# At least 20 rows
csv_path = Path(__file__).parent.parent / "data" / "titanic.csv"
df = pd.read_csv(csv_path)

print("Titanic data (sample):")
print(df.head())

# --- Bar chart: survival rate by class ---
survival_by_class = pd.DataFrame(
    df.groupby("Pclass", as_index=False).agg(survived_mean=("Survived", "mean"))
)
survival_by_class["survival_rate_pct"] = survival_by_class["survived_mean"] * 100
class_labels = [str(value) for value in survival_by_class["Pclass"]]
class_rates = [float(value) for value in survival_by_class["survival_rate_pct"]]

plt.figure(figsize=(7, 5))
plt.bar(class_labels, class_rates, color=["gold", "silver", "chocolate"])
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
survival_by_sex = pd.DataFrame(
    df.groupby("Sex", as_index=False).agg(
        survived_sum=("Survived", "sum"),
        total_count=("Survived", "count"),
    )
)
survival_by_sex["survived_pct"] = (
    survival_by_sex["survived_sum"] / survival_by_sex["total_count"] * 100
)
survival_by_sex["died_pct"] = 100 - survival_by_sex["survived_pct"]
survived_pct = [float(value) for value in survival_by_sex["survived_pct"]]
died_pct = [float(value) for value in survival_by_sex["died_pct"]]
sex_labels = [str(value) for value in survival_by_sex["Sex"]]

x = np.arange(len(sex_labels))
width = 0.35
fig, ax = plt.subplots(figsize=(7, 5))
ax.bar(x - width / 2, survived_pct, width, label="Survived", color="green")
ax.bar(x + width / 2, died_pct, width, label="Died", color="red")
ax.set_xticks(x)
ax.set_xticklabels(sex_labels)
ax.set_ylabel("Percentage")
ax.set_title("Survival by Gender")
ax.legend()
plt.tight_layout()
plt.savefig("titanic_survival_by_gender.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Pie chart: passenger class distribution ---
class_counts = pd.DataFrame(
    df.groupby("Pclass", as_index=False).agg(count=("Pclass", "size"))
)
class_count_rows = sorted(
    class_counts.itertuples(index=False),
    key=lambda row: int(row[0]),
)
class_counts = pd.DataFrame(class_count_rows, columns=["Pclass", "count"])
pie_values = [float(value) for value in class_counts["count"]]
pie_labels = [f"Class {value}" for value in class_counts["Pclass"]]

plt.figure(figsize=(6, 6))
plt.pie(pie_values, labels=pie_labels, autopct="%1.1f%%", startangle=90)
plt.title("Passenger Class Distribution")
plt.tight_layout()
plt.savefig("titanic_pie_class.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Box plot: fare distribution by class ---
df_box = pd.DataFrame(df.loc[:, ["Pclass", "Fare"]]).copy()
df_box["Pclass"] = df_box["Pclass"].astype(str)

plt.figure(figsize=(7, 5))
df_box.boxplot(column="Fare", by="Pclass", ax=plt.gca())
plt.suptitle("")
plt.title("Fare Distribution by Class")
plt.xlabel("Class")
plt.ylabel("Fare")
plt.tight_layout()
plt.savefig("titanic_fare_boxplot.png", dpi=100, bbox_inches="tight")
plt.show()

print("Plots saved: titanic_survival_by_class.png, titanic_age_histogram.png, titanic_survival_by_gender.png, titanic_pie_class.png, titanic_fare_boxplot.png")
