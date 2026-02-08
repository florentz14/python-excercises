# -------------------------------------------------
# File Name: 33_tips_viz.py
# Author: Florentino Báez
# Date: Pandas
# Description: Visualize Restaurant Tips Data. Create scatter plots, box plots,
#              and categorical charts analyzing tips by meal, day, and party size.
# -------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create tips DataFrame: total_bill, tip, sex, smoker, day, time, size
# At least 20 rows
np.random.seed(42)
n = 24
data = {
    "total_bill": np.round(np.random.uniform(8, 45, n), 2),
    "tip": np.round(np.random.uniform(1, 8, n), 2),
    "sex": np.random.choice(["Male", "Female"], n),
    "smoker": np.random.choice(["Yes", "No"], n),
    "day": np.random.choice(["Fri", "Sat", "Sun", "Thur"], n),
    "time": np.random.choice(["Lunch", "Dinner"], n),
    "size": np.random.randint(1, 6, n)
}

df = pd.DataFrame(data)

# Calculate tip_percentage for analysis
df["tip_percentage"] = (df["tip"] / df["total_bill"] * 100).round(2)

print("Tips data (sample):")
print(df.head())

# --- Scatter plot: total_bill vs tip ---
plt.figure(figsize=(7, 5))
plt.scatter(df["total_bill"], df["tip"], alpha=0.7)
plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.tight_layout()
plt.savefig("tips_bill_vs_tip.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Box plot: tip distribution by day ---
df_tip_day = df[["day", "tip"]]
days_order = ["Thur", "Fri", "Sat", "Sun"]
df_tip_day["day"] = pd.Categorical(df_tip_day["day"], categories=days_order, ordered=True)
df_tip_day = df_tip_day.sort_values("day")

plt.figure(figsize=(7, 5))
df.boxplot(column="tip", by="day")
plt.suptitle("")
plt.title("Tip Distribution by Day")
plt.xlabel("Day")
plt.ylabel("Tip ($)")
plt.tight_layout()
plt.savefig("tips_boxplot_by_day.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Bar chart: average tip by meal time (Lunch vs Dinner) ---
avg_tip_by_time = df.groupby("time")["tip"].mean()

plt.figure(figsize=(6, 5))
plt.bar(avg_tip_by_time.index, avg_tip_by_time.values, color=["steelblue", "coral"], edgecolor="black")
plt.title("Average Tip by Meal Time")
plt.xlabel("Meal Time")
plt.ylabel("Average Tip ($)")
plt.tight_layout()
plt.savefig("tips_avg_by_time.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Histogram: total bill distribution ---
plt.figure(figsize=(7, 5))
plt.hist(df["total_bill"], bins=10, color="seagreen", edgecolor="black")
plt.title("Total Bill Distribution")
plt.xlabel("Total Bill ($)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("tips_bill_histogram.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Grouped bar chart: average tip by day and smoker status ---
pivot_tip = df.pivot_table(values="tip", index="day", columns="smoker", aggfunc="mean", fill_value=0)
# Ensure day order
pivot_tip = pivot_tip.reindex(days_order)

x = np.arange(len(pivot_tip.index))
width = 0.35
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(x - width/2, pivot_tip["No"], width, label="Non-Smoker")
ax.bar(x + width/2, pivot_tip["Yes"], width, label="Smoker")
ax.set_xticks(x)
ax.set_xticklabels(pivot_tip.index)
ax.set_ylabel("Average Tip ($)")
ax.set_title("Average Tip by Day and Smoker Status")
ax.legend()
plt.tight_layout()
plt.savefig("tips_by_day_smoker.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Histogram: tip_percentage ---
plt.figure(figsize=(7, 5))
plt.hist(df["tip_percentage"], bins=10, color="purple", edgecolor="black", alpha=0.8)
plt.title("Tip Percentage Distribution")
plt.xlabel("Tip (%)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("tips_pct_histogram.png", dpi=100, bbox_inches="tight")
plt.show()

print("Plots saved: tips_bill_vs_tip.png, tips_boxplot_by_day.png, tips_avg_by_time.png, tips_bill_histogram.png, tips_by_day_smoker.png, tips_pct_histogram.png")
