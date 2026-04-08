# -------------------------------------------------
# File Name: 35_baby_names_stats.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Rank, nunique, std, variance, and trends in baby names.
# -------------------------------------------------

import pandas as pd
import numpy as np
from pathlib import Path

df = pd.read_csv(Path(__file__).parent.parent / "data" / "us_baby_names.csv")

print("=" * 60)
print("US BABY NAMES - STATISTICAL ANALYSIS")
print("=" * 60)

# Use describe() for summary statistics on numeric columns
print("\n--- Summary statistics (describe) ---")
print(df.describe())

# Find most popular name per year using groupby + idxmax
print("\n--- Most popular name per year (by total count) ---")
year_name_counts = df.groupby(["Year", "Name", "Gender"], as_index=False).agg(Count=("Count", "sum"))
year_name_rows = sorted(
    year_name_counts.itertuples(index=False),
    key=lambda row: (int(row[0]), -int(row[3])),
)
most_popular_per_year = (
    pd.DataFrame(year_name_rows, columns=["Year", "Name", "Gender", "Count"])
    .drop_duplicates("Year")
    .set_index("Year")
)
print(most_popular_per_year)

# Calculate total births per year
print("\n--- Total births per year ---")
total_births_per_year = df.groupby("Year")["Count"].sum()
print(total_births_per_year)

# Find top 5 names overall by total count
print("\n--- Top 5 names overall by total count ---")
top5_overall = (
    df.groupby("Name", as_index=False)
    .agg(Count=("Count", "sum"))
)
top5_rows = sorted(
    top5_overall.itertuples(index=False),
    key=lambda row: int(row[1]),
    reverse=True,
)[:5]
top5_overall = pd.DataFrame(top5_rows, columns=["Name", "Count"]).set_index("Name")["Count"]
print(top5_overall)

# Calculate percentage each name represents of yearly total
print("\n--- Percentage of yearly total (sample: first 5 rows) ---")
year_totals = df.groupby("Year")["Count"].transform("sum")
df["PctOfYear"] = (df["Count"] / year_totals * 100).round(2)
print(df[["Name", "Year", "Count", "PctOfYear"]].head())

# Use rank() to rank names within each year (descending by count)
print("\n--- Rank of names within each year ---")
df["RankInYear"] = df.groupby("Year")["Count"].rank(ascending=False, method="min")
print(
    pd.DataFrame(
        sorted(
            df[["Name", "Year", "Count", "RankInYear"]].itertuples(index=False),
            key=lambda row: (int(row[1]), float(row[3])),
        )[:10],
        columns=["Name", "Year", "Count", "RankInYear"],
    )
)

# Compare male vs female name diversity (nunique per gender)
print("\n--- Name diversity: unique names per gender ---")
diversity = df.groupby("Gender")["Name"].nunique()
print(diversity)

# Show standard deviation and variance of name counts
print("\n--- Standard deviation of name counts (overall) ---")
print(f"Std: {df['Count'].std():.2f}")
print("\n--- Variance of name counts (overall) ---")
print(f"Variance: {df['Count'].var():.2f}")
print("\n--- Std and variance per year ---")
print(df.groupby("Year")["Count"].agg(["std", "var"]))

print("\nDone.")
