# -------------------------------------------------
# File Name: 24_merge_auto_mpg.py
# Author: Florentino Báez
# Date: Pandas
# Description: Merge Auto MPG Datasets. Practice pd.merge() with different join
#              types (inner, left, right, outer) on automobile performance and
#              specification data.
# -------------------------------------------------

import pandas as pd
from pathlib import Path

df_cars = pd.read_csv(Path(__file__).parent / "auto_mpg_cars.csv")
df_origin = pd.read_csv(Path(__file__).parent / "auto_mpg_origin.csv")

print("=" * 60)
print("DF_CARS (car_name, mpg, cylinders, displacement, horsepower)")
print("=" * 60)
print(df_cars)
print()
print("DF_ORIGIN (car_name, origin, model_year, weight)")
print("=" * 60)
print(df_origin)
print()

# Inner merge on car_name: only rows with matching key in both
inner = pd.merge(df_cars, df_origin, on="car_name", how="inner")
print("INNER merge on car_name:")
print(inner)
print(f"Shape after inner merge: {inner.shape}")
print()

# Left merge on car_name: all from left (df_cars), match from right
left = pd.merge(df_cars, df_origin, on="car_name", how="left")
print("LEFT merge on car_name (all cars from df_cars):")
print(left)
print(f"Shape after left merge: {left.shape}")
print()

# Right merge on car_name: all from right (df_origin), match from left
right = pd.merge(df_cars, df_origin, on="car_name", how="right")
print("RIGHT merge on car_name (all cars from df_origin):")
print(right)
print(f"Shape after right merge: {right.shape}")
print()

# Outer merge on car_name: all rows from both, NaN where no match
outer = pd.merge(df_cars, df_origin, on="car_name", how="outer")
print("OUTER merge on car_name:")
print(outer)
print(f"Shape after outer merge: {outer.shape}")
print()

# Show how each join type affects row count
print("Row count summary:")
print(f"  df_cars: {len(df_cars)}, df_origin: {len(df_origin)}")
print(f"  inner: {len(inner)}, left: {len(left)}, right: {len(right)}, outer: {len(outer)}")
print()

# Merge and then filter: only cars with mpg > 25 (add a high-mpg car for demo)
df_cars_extra = pd.concat([df_cars, pd.DataFrame({"car_name": ["toyota corolla"], "mpg": [28.0], "cylinders": [4], "displacement": [97.0], "horsepower": [88.0]})], ignore_index=True)
merged_all = pd.merge(df_cars_extra, df_origin, on="car_name", how="left")
filtered = merged_all[merged_all["mpg"] > 25]
print("Merged then filtered (mpg > 25):")
print(filtered)
print()

# Use suffixes parameter when columns overlap (e.g. if both had 'value')
df_left = pd.DataFrame({"car_name": ["a", "b"], "value": [1, 2]})
df_right = pd.DataFrame({"car_name": ["a", "b"], "value": [10, 20]})
with_suffixes = pd.merge(df_left, df_right, on="car_name", suffixes=("_left", "_right"))
print("Merge with suffixes (when columns overlap):")
print(with_suffixes)
print()

# Print shape after each merge to show differences
print("Shape summary: inner {}, left {}, right {}, outer {}".format(inner.shape[0], left.shape[0], right.shape[0], outer.shape[0]))
