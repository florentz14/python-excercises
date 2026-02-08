# -------------------------------------------------
# File Name: 25_merge_fictitious_names.py
# Author: Florentino Báez
# Date: Pandas
# Description: Merge Fictitious Name Datasets. Practice merging on multiple keys,
#              concatenation with pd.concat(), and append-like operations on
#              people data.
# -------------------------------------------------

import pandas as pd
from pathlib import Path

df_personal = pd.read_csv(Path(__file__).parent / "fictitious_personal.csv")
df_work = pd.read_csv(Path(__file__).parent / "fictitious_work.csv")
df_education = pd.read_csv(Path(__file__).parent / "fictitious_education.csv")

print("=" * 60)
print("DF_PERSONAL (first_name, last_name, age, city)")
print("=" * 60)
print(df_personal)
print()
print("DF_WORK (first_name, last_name, company, salary)")
print("=" * 60)
print(df_work)
print()
print("DF_EDUCATION (first_name, last_name, degree, university)")
print("=" * 60)
print(df_education)
print()

# Merge df_personal and df_work on [first_name, last_name]
merged_personal_work = pd.merge(df_personal, df_work, on=["first_name", "last_name"], how="inner")
print("Merge df_personal and df_work on [first_name, last_name] (inner):")
print(merged_personal_work)
print()

# Merge all three DataFrames step by step
merged_two = pd.merge(df_personal, df_work, on=["first_name", "last_name"], how="left")
merged_three = pd.merge(merged_two, df_education, on=["first_name", "last_name"], how="left")
print("Merge all three step by step (personal -> work -> education):")
print(merged_three)
print()

# Use pd.concat() to stack DataFrames vertically (same columns)
# Create two small tables with same structure for vertical concat
df_a = df_personal.head(3)
df_b = df_personal.tail(2)
vertical = pd.concat([df_a, df_b], axis=0, ignore_index=True)
print("pd.concat(axis=0) - stack vertically:")
print(vertical)
print()

# Use pd.concat() with axis=1 to join side by side (by index)
df_left = df_personal[["first_name", "last_name"]].head(5)
df_right = df_work[["company", "salary"]].head(5)
side_by_side = pd.concat([df_left.reset_index(drop=True), df_right.reset_index(drop=True)], axis=1)
print("pd.concat(axis=1) - join side by side (by position):")
print(side_by_side)
print()

# Show indicator=True to see merge source (_merge column)
merged_indicator = pd.merge(df_personal, df_work, on=["first_name", "last_name"], how="outer", indicator=True)
print("Merge with indicator=True (_merge column):")
print(merged_indicator)
print()

# Demonstrate validate parameter: one-to-one or many-to-one
# validate='1:1' raises if duplicate keys in either side
merged_validate = pd.merge(df_personal.head(5), df_work.head(5), on=["first_name", "last_name"], how="inner", validate="1:1")
print("Merge with validate='1:1' (no duplicate keys):")
print(merged_validate)
print()

# Handle duplicate keys: show what happens with duplicates
df_dup = pd.DataFrame({"first_name": ["John", "John"], "last_name": ["Smith", "Smith"], "score": [90, 85]})
merged_dup = pd.merge(df_personal.head(1), df_dup, on=["first_name", "last_name"])
print("Merge with duplicate keys in right (creates multiple rows):")
print(merged_dup)
