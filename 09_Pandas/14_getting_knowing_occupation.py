# -------------------------------------------------
# File Name: 14_getting_knowing_occupation.py
# Author: Florentino Báez
# Date: Pandas
# Description: Explore the Occupation Dataset. Load user data with age,
#              gender, occupation, and zip code. Examine structure,
#              unique values, and basic statistics.
# -------------------------------------------------

import pandas as pd
from pathlib import Path

# Load user/occupation data from the CSV file (same folder as this script)
csv_path = Path(__file__).parent / "occupation_users.csv"
df = pd.read_csv(csv_path, dtype={"zip_code": str})

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
