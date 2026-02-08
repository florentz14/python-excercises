# -------------------------------------------------
# File Name: 31_visualization_scores.py
# Author: Florentino Báez
# Date: Pandas
# Description: Visualize Student Scores Data. Create scatter plots, box plots,
#              and histograms to compare math, reading, and writing scores.
# -------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create scores DataFrame: student_id, gender, math_score, reading_score, writing_score
# At least 20 rows
np.random.seed(42)
n = 22
data = {
    "student_id": range(1, n + 1),
    "gender": np.random.choice(["M", "F"], n),
    "math_score": np.random.randint(50, 100, n),
    "reading_score": np.random.randint(50, 100, n),
    "writing_score": np.random.randint(50, 100, n),
}

df = pd.DataFrame(data)

print("Scores data (sample):")
print(df.head())

# --- Scatter plot: math vs reading scores (color by gender) ---
fig, ax = plt.subplots(figsize=(7, 6))
for g in df["gender"].unique():
    subset = df[df["gender"] == g]
    ax.scatter(subset["math_score"], subset["reading_score"], label=g, alpha=0.7)
ax.set_xlabel("Math Score")
ax.set_ylabel("Reading Score")
ax.set_title("Math vs Reading Scores (by Gender)")
ax.legend()
plt.tight_layout()
plt.savefig("scores_math_vs_reading.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Histogram: distribution of math scores ---
plt.figure(figsize=(7, 5))
plt.hist(df["math_score"], bins=10, color="steelblue", edgecolor="black")
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("scores_math_histogram.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Box plot: all three scores side by side ---
plt.figure(figsize=(8, 5))
df[["math_score", "reading_score", "writing_score"]].boxplot()
plt.title("Score Distributions: Math, Reading, Writing")
plt.ylabel("Score")
plt.tight_layout()
plt.savefig("scores_boxplot.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Bar chart: average scores by gender ---
avg_by_gender = df.groupby("gender")[["math_score", "reading_score", "writing_score"]].mean()

x = np.arange(len(avg_by_gender.columns))
width = 0.35
fig, ax = plt.subplots(figsize=(7, 5))
for i, (g, row) in enumerate(avg_by_gender.iterrows()):
    ax.bar(x + i * width - width/2, row.values, width, label=g)
ax.set_xticks(x)
ax.set_xticklabels(avg_by_gender.columns)
ax.set_ylabel("Average Score")
ax.set_title("Average Scores by Gender")
ax.legend()
plt.tight_layout()
plt.savefig("scores_avg_by_gender.png", dpi=100, bbox_inches="tight")
plt.show()

# --- Line chart: cumulative distribution of writing scores (sorted) ---
sorted_writing = np.sort(df["writing_score"])
cumulative = np.arange(1, len(sorted_writing) + 1) / len(sorted_writing) * 100

plt.figure(figsize=(7, 5))
plt.plot(sorted_writing, cumulative, marker=".", markersize=4)
plt.title("Cumulative Distribution of Writing Scores")
plt.xlabel("Writing Score")
plt.ylabel("Cumulative Percentage (%)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("scores_writing_cumulative.png", dpi=100, bbox_inches="tight")
plt.show()

print("Plots saved: scores_math_vs_reading.png, scores_math_histogram.png, scores_boxplot.png, scores_avg_by_gender.png, scores_writing_cumulative.png")
