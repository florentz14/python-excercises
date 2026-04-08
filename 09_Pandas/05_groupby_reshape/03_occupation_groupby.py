# -------------------------------------------------
# File Name: 28_occupation_groupby.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Mean age per occupation, gender ratio, aggregation.
# -------------------------------------------------

import pandas as pd
from pathlib import Path

csv_path = Path(__file__).parent.parent / "data" / "grouping_occupation_users.csv"
df = pd.read_csv(csv_path, dtype={"zip_code": str})

print("=" * 60)
print("ORIGINAL DATAFRAME (user_id, age, gender, occupation, zip_code)")
print("=" * 60)
print(df)
print()

# Group by occupation, find mean age per occupation
mean_age_by_occupation = df.groupby("occupation", as_index=False).agg(mean_age=("age", "mean"))
print("Mean age per occupation:")
print(mean_age_by_occupation)
print()

# Group by occupation, count users per occupation
users_per_occupation = df.groupby("occupation").size()
print("Count of users per occupation:")
print(users_per_occupation)
print()

# Group by occupation AND gender, count entries
occupation_gender_counts = df.groupby(["occupation", "gender"]).size()
print("Count by occupation and gender:")
print(occupation_gender_counts)
print()

# Find occupation with the oldest average age
oldest_row = max(
    mean_age_by_occupation.itertuples(index=False),
    key=lambda row: float(row[1]),
)
print(f"Occupation with oldest average age: {oldest_row[0]} ({float(oldest_row[1]):.2f} years)")
print()

# Use agg() to get min, max, mean age per occupation
age_agg = df.groupby("occupation")["age"].agg(["min", "max", "mean"])
print("Min, max, mean age per occupation (agg):")
print(age_agg)
print()

# Calculate gender ratio per occupation (e.g., proportion of M per occupation)
gender_counts = df.groupby(["occupation", "gender"]).size().unstack(fill_value=0)
gender_ratio = gender_counts["M"] / (gender_counts["M"] + gender_counts["F"])
print("Gender ratio (proportion Male) per occupation:")
print(gender_ratio)
print()

# Sort occupations by average age
sorted_rows = sorted(
    mean_age_by_occupation.itertuples(index=False),
    key=lambda row: float(row[1]),
    reverse=True,
)
sorted_occupations = pd.DataFrame(sorted_rows, columns=["occupation", "mean_age"])
print("Occupations sorted by average age (descending):")
print(sorted_occupations)
