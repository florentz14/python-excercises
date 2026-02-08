# -------------------------------------------------
# File Name: 14_getting_knowing_occupation.py
# Author: Florentino Báez
# Date: Pandas
# Description: Explore the Occupation Dataset. Load user data with age,
#              gender, occupation, and zip code. Examine structure,
#              unique values, and basic statistics.
# -------------------------------------------------

import pandas as pd

# Create sample user/occupation data inline (no external CSV)
users_data = {
    "user_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    "age": [24, 53, 23, 24, 33, 42, 57, 36, 29, 53, 39, 28, 47, 45, 31],
    "gender": ["M", "F", "M", "M", "F", "M", "M", "F", "F", "M", "F", "M", "F", "M", "F"],
    "occupation": [
        "technician",
        "educator",
        "engineer",
        "student",
        "engineer",
        "educator",
        "executive",
        "administrator",
        "student",
        "lawyer",
        "technician",
        "engineer",
        "educator",
        "engineer",
        "lawyer",
    ],
    "zip_code": [
        "85711",
        "94043",
        "32067",
        "43537",
        "15213",
        "98101",
        "91344",
        "05201",
        "01002",
        "90703",
        "30329",
        "06511",
        "29205",
        "55106",
        "43202",
    ],
}

df = pd.DataFrame(users_data)

# Show first 5 rows
print("=== HEAD (first 5 rows) ===")
print(df.head())
print()

# Show last 5 rows
print("=== TAIL (last 5 rows) ===")
print(df.tail())
print()

# Shape of the DataFrame
print("=== SHAPE ===")
print(df.shape)
print()

# Data types for each column
print("=== DTYPES ===")
print(df.dtypes)
print()

# Number of unique occupations
print("=== UNIQUE OCCUPATIONS ===")
num_occupations = df["occupation"].nunique()
print(f"Number of unique occupations: {num_occupations}")
print(f"Unique occupations: {df['occupation'].unique().tolist()}")
print()

# Most frequent occupation
print("=== MOST FREQUENT OCCUPATION ===")
most_frequent = df["occupation"].value_counts().idxmax()
count = df["occupation"].value_counts().iloc[0]
print(f"Most frequent occupation: {most_frequent} (count: {count})")
print("Full value_counts:")
print(df["occupation"].value_counts())
print()

# Summarize the DataFrame using describe()
print("=== DESCRIBE (numeric summary) ===")
print(df.describe())
print()

# Age distribution: mean, min, max
print("=== AGE DISTRIBUTION ===")
print(f"Mean age: {df['age'].mean():.2f}")
print(f"Min age: {df['age'].min()}")
print(f"Max age: {df['age'].max()}")
print()

# Count users per occupation
print("=== USERS PER OCCUPATION ===")
users_per_occupation = df["occupation"].value_counts().sort_index()
print(users_per_occupation)
