# -------------------------------------------------
# File Name: 29_regiment_groupby.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Regiment/company scores, improvement, multi-aggregation.
# -------------------------------------------------

import pandas as pd
from pathlib import Path

csv_path = Path(__file__).parent.parent / "data" / "regiment.csv"
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
post_means = df.groupby("regiment", as_index=False).agg(
    mean_post_test_score=("postTestScore", "mean")
)
best_regiment_row = max(
    post_means.itertuples(index=False),
    key=lambda row: float(row[1]),
)
print(
    "Regiment with highest average postTestScore: "
    f"{best_regiment_row[0]} ({float(best_regiment_row[1]):.2f})"
)
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
