# -------------------------------------------------
# File Name: 27_baby_names_stats.py
# Author: Florentino Báez
# Date: Pandas
# Description: Statistical Analysis of US Baby Names. Compute frequency counts,
#              rank names, analyze trends over years, and find most popular
#              names using pandas statistical methods.
# -------------------------------------------------

import pandas as pd
import numpy as np
from pathlib import Path

df = pd.read_csv(Path(__file__).parent / "us_baby_names.csv")

print("=" * 60)
print("US BABY NAMES - STATISTICAL ANALYSIS")
print("=" * 60)

# Use describe() for summary statistics on numeric columns
print("\n--- Summary statistics (describe) ---")
print(df.describe())

# Find most popular name per year using groupby + idxmax
print("\n--- Most popular name per year (by total count) ---")
idx_max = df.groupby("Year")["Count"].idxmax()
most_popular_per_year = df.loc[idx_max, ["Year", "Name", "Gender", "Count"]].set_index("Year")
print(most_popular_per_year)

# Calculate total births per year
print("\n--- Total births per year ---")
total_births_per_year = df.groupby("Year")["Count"].sum()
print(total_births_per_year)

# Find top 5 names overall by total count
print("\n--- Top 5 names overall by total count ---")
top5_overall = df.groupby("Name")["Count"].sum().nlargest(5)
print(top5_overall)

# Calculate percentage each name represents of yearly total
print("\n--- Percentage of yearly total (sample: first 5 rows) ---")
year_totals = df.groupby("Year")["Count"].transform("sum")
df["PctOfYear"] = (df["Count"] / year_totals * 100).round(2)
print(df[["Name", "Year", "Count", "PctOfYear"]].head())

# Use rank() to rank names within each year (descending by count)
print("\n--- Rank of names within each year ---")
df["RankInYear"] = df.groupby("Year")["Count"].rank(ascending=False, method="min")
print(df[["Name", "Year", "Count", "RankInYear"]].sort_values(["Year", "RankInYear"]).head(10))

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
