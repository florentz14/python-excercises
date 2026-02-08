# -------------------------------------------------
# File Name: 21_grouping_regiment.py
# Author: Florentino Báez
# Date: Pandas
# Description: Group and Aggregate Regiment Data. Practice groupby on military
#              unit data to analyze test scores, company performance, and
#              regiment comparisons.
# -------------------------------------------------

import pandas as pd
from pathlib import Path

csv_path = Path(__file__).parent / "regiment.csv"
df = pd.read_csv(csv_path)

print("=" * 60)
print("ORIGINAL DATAFRAME (regiment, company, name, preTestScore, postTestScore)")
print("=" * 60)
print(df)
print()

# Group by regiment, get mean of preTestScore and postTestScore
regiment_means = df.groupby("regiment")[["preTestScore", "postTestScore"]].mean()
print("Mean preTestScore and postTestScore per regiment:")
print(regiment_means)
print()

# Group by regiment and company, count soldiers
soldiers_per_regiment_company = df.groupby(["regiment", "company"]).size()
print("Count of soldiers per regiment and company:")
print(soldiers_per_regiment_company)
print()

# Find regiment with highest average postTestScore
post_means = df.groupby("regiment")["postTestScore"].mean()
best_regiment = post_means.idxmax()
print(f"Regiment with highest average postTestScore: {best_regiment} ({post_means.max():.2f})")
print()

# Calculate average improvement (post - pre) per regiment
df["improvement"] = df["postTestScore"] - df["preTestScore"]
avg_improvement = df.groupby("regiment")["improvement"].mean()
print("Average improvement (post - pre) per regiment:")
print(avg_improvement)
print()

# Use agg() with multiple functions on scores
score_agg = df.groupby("regiment")[["preTestScore", "postTestScore"]].agg(["mean", "min", "max"])
print("Aggregate (mean, min, max) on scores per regiment:")
print(score_agg)
print()

# Group by company, find max postTestScore
max_post_by_company = df.groupby("company")["postTestScore"].max()
print("Max postTestScore per company:")
print(max_post_by_company)
print()

# Show number of soldiers per regiment
soldiers_per_regiment = df.groupby("regiment").size()
print("Number of soldiers per regiment:")
print(soldiers_per_regiment)
