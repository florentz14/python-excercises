# -------------------------------------------------
# File Name: 19_alcohol_groupby.py
# Author: Florentino Báez
# Date: Pandas
# Description: Group and Aggregate Alcohol Consumption Data. Practice
#              groupby(), agg(), mean(), sum(), and multi-level
#              aggregation on alcohol consumption by country and continent.
# -------------------------------------------------

import pandas as pd
from pathlib import Path

csv_path = Path(__file__).parent / "alcohol_consumption.csv"
df = pd.read_csv(csv_path)

# Group by continent and calculate mean of all numeric columns
print("=== GROUP BY continent: mean of numeric columns ===")
continent_means = df.groupby("continent").mean(numeric_only=True)
print(continent_means)
print()

# Find continent with highest beer consumption (mean)
print("=== CONTINENT WITH HIGHEST BEER CONSUMPTION (mean) ===")
beer_by_continent = df.groupby("continent")["beer_servings"].mean()
highest_beer_continent = beer_by_continent.idxmax()
print(f"Continent: {highest_beer_continent}, Mean beer servings: {beer_by_continent.max():.1f}")
print(beer_by_continent.sort_values(ascending=False))
print()

# Calculate total litres per continent (sum)
print("=== TOTAL LITRES PER CONTINENT ===")
total_litres_continent = df.groupby("continent")["total_litres"].sum()
print(total_litres_continent)
print()

# Use agg() with multiple functions (mean, min, max, std)
print("=== AGG: mean, min, max, std per continent (beer_servings) ===")
agg_result = df.groupby("continent")["beer_servings"].agg(["mean", "min", "max", "std"])
print(agg_result)
print()

# Find the country with the max wine_servings per continent
print("=== COUNTRY WITH MAX wine_servings PER CONTINENT ===")
idx_max_wine = df.groupby("continent")["wine_servings"].idxmax()
max_wine_countries = df.loc[idx_max_wine, ["continent", "country", "wine_servings"]]
print(max_wine_countries)
print()

# Group and count countries per continent
print("=== COUNT OF COUNTRIES PER CONTINENT ===")
count_per_continent = df.groupby("continent").size()
print(count_per_continent)
print()

# Median alcohol consumption (total_litres) per continent
print("=== MEDIAN total_litres PER CONTINENT ===")
median_alcohol = df.groupby("continent")["total_litres"].median()
print(median_alcohol)
