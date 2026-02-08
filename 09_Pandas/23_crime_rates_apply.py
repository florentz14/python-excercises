# -------------------------------------------------
# File Name: 23_crime_rates_apply.py
# Author: Florentino Báez
# Date: Pandas
# Description: Apply Functions to US Crime Rate Data. Use apply() to compute
#              per-capita rates, percent changes, and classify crime levels
#              from yearly statistics.
# -------------------------------------------------

import pandas as pd
from pathlib import Path

df = pd.read_csv(Path(__file__).parent / "us_crime_rates.csv")

print("=" * 60)
print("ORIGINAL DATAFRAME (Year, Population, Total, Violent, Property, Murder, Robbery, Burglary)")
print("=" * 60)
print(df)
print()

# Crime columns to compute per-capita rates
crime_cols = ["Total", "Violent", "Property", "Murder", "Robbery", "Burglary"]

# Use apply() to calculate crime rate per 100,000 population for each crime type
for col in crime_cols:
    df[f"{col}_rate"] = (df[col] / df["Population"]) * 100_000
print("Crime rates per 100,000 population (sample columns):")
print(df[["Year", "Total_rate", "Murder_rate", "Violent_rate"]])
print()

# Apply a custom function to classify years as 'High Crime' or 'Low Crime' based on total
median_total = df["Total"].median()
def classify_crime(total):
    return "High Crime" if total >= median_total else "Low Crime"

df["crime_level"] = df["Total"].apply(classify_crime)
print("Year classified by total crime (High/Low relative to median):")
print(df[["Year", "Total", "crime_level"]])
print()

# Calculate year-over-year percent change using pct_change()
df["Total_pct_change"] = df["Total"].pct_change() * 100
print("Year-over-year percent change in Total crime:")
print(df[["Year", "Total", "Total_pct_change"]])
print()

# Use apply(axis=1) to sum all crime categories per row
df["sum_crime_categories"] = df.apply(
    lambda row: row["Violent"] + row["Property"] + row["Murder"] + row["Robbery"] + row["Burglary"],
    axis=1,
)
print("Sum of crime categories per row:")
print(df[["Year", "sum_crime_categories"]])
print()

# Create 'violent_ratio' column = Violent / Total using apply
df["violent_ratio"] = df.apply(lambda row: row["Violent"] / row["Total"] if row["Total"] > 0 else 0, axis=1)
print("Violent ratio (Violent/Total):")
print(df[["Year", "Violent", "Total", "violent_ratio"]])
print()

# Normalize all crime columns to 0-1 range using apply
for col in crime_cols:
    df[f"{col}_norm"] = df[col].apply(lambda x, c=col: (x - df[c].min()) / (df[c].max() - df[c].min()) if df[c].max() != df[c].min() else 0)
print("Normalized crime columns (0-1 range) - Total_norm and Murder_norm:")
print(df[["Year", "Total_norm", "Murder_norm"]])
print()

# Find the year with the highest murder rate per capita
year_max_murder = df.loc[df["Murder_rate"].idxmax(), "Year"]
print(f"Year with highest murder rate per capita: {int(year_max_murder)}")
print(df[["Year", "Murder", "Population", "Murder_rate"]].sort_values("Murder_rate", ascending=False).head(3))
