# -------------------------------------------------
# File Name: 27_alcohol_groupby.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: GroupBy by continent with mean/min/max/std and median.
# -------------------------------------------------

import pandas as pd
from pathlib import Path

csv_path = Path(__file__).parent.parent / "data" / "alcohol_consumption.csv"
df = pd.read_csv(csv_path)

# Group by continent and calculate mean of all numeric columns
print("=== GROUP BY continent: mean of numeric columns ===")
continent_means = df.groupby("continent").mean(numeric_only=True)
print(continent_means)
print()

# Find continent with highest beer consumption (mean)
print("=== CONTINENT WITH HIGHEST BEER CONSUMPTION (mean) ===")
beer_by_continent = df.groupby("continent", as_index=False).agg(
    mean_beer_servings=("beer_servings", "mean")
)
sorted_rows = sorted(
    beer_by_continent.itertuples(index=False),
    key=lambda row: float(row[1]),
    reverse=True,
)
beer_by_continent_sorted = pd.DataFrame(
    sorted_rows, columns=["continent", "mean_beer_servings"]
)
highest_beer_row = beer_by_continent_sorted.iloc[0]
print(
    f"Continent: {highest_beer_row['continent']}, "
    f"Mean beer servings: {highest_beer_row['mean_beer_servings']:.1f}"
)
print(beer_by_continent_sorted)
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
max_wine_countries = (
    df.sort_values(["continent", "wine_servings"], ascending=[True, False])
    .drop_duplicates("continent")
    [["continent", "country", "wine_servings"]]
)
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
