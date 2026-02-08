# -------------------------------------------------
# File Name: 20_grouping_occupation.py
# Author: Florentino Báez
# Date: Pandas
# Description: Group and Aggregate Occupation Data. Practice groupby on user
#              demographic data to analyze age statistics, gender distribution,
#              and counts per occupation.
# -------------------------------------------------

import pandas as pd

# Create sample user demographic data (inline, no external CSV)
data = {
    "user_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    "age": [25, 32, 28, 45, 22, 38, 29, 51, 27, 34, 41, 23, 36, 44, 30],
    "gender": ["M", "F", "M", "M", "F", "F", "M", "F", "M", "F", "M", "F", "M", "F", "M"],
    "occupation": [
        "engineer", "teacher", "engineer", "doctor", "student",
        "teacher", "engineer", "doctor", "student", "teacher",
        "doctor", "student", "engineer", "nurse", "nurse",
    ],
    "zip_code": ["10001", "10002", "10003", "10004", "10005", "10006", "10007", "10008", "10009", "10010", "10011", "10012", "10013", "10014", "10015"],
}
df = pd.DataFrame(data)

print("=" * 60)
print("ORIGINAL DATAFRAME (user_id, age, gender, occupation, zip_code)")
print("=" * 60)
print(df)
print()

# Group by occupation, find mean age per occupation
mean_age_by_occupation = df.groupby("occupation")["age"].mean()
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
oldest_avg_occupation = mean_age_by_occupation.idxmax()
print(f"Occupation with oldest average age: {oldest_avg_occupation} ({mean_age_by_occupation.max():.2f} years)")
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
sorted_occupations = mean_age_by_occupation.sort_values(ascending=False)
print("Occupations sorted by average age (descending):")
print(sorted_occupations)
