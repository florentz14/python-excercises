# -------------------------------------------------
# File Name: 15_food_facts_explore.py
# Author: Florentino Báez
# Date: Pandas
# Description: Explore the World Food Facts Dataset. Load food product data
#              with nutrition info. Use info(), describe(), columns, and
#              isnull() to understand data quality.
# -------------------------------------------------

import pandas as pd
from pathlib import Path

# Load food product data from the CSV file (same folder as this script)
# Empty cells in the CSV are automatically read as NaN by pandas
csv_path = Path(__file__).parent / "world_food_facts.csv"
df = pd.read_csv(csv_path)

# Print shape
print("=== SHAPE ===")
print(df.shape)
print()

# Print column names
print("=== COLUMNS ===")
print(df.columns.tolist())
print()

# Print data types
print("=== DTYPES ===")
print(df.dtypes)
print()

# Count null values per column with isnull().sum()
print("=== NULL VALUES PER COLUMN ===")
null_counts = df.isnull().sum()
print(null_counts)
print()

# Percentage of missing values per column
print("=== PERCENTAGE OF MISSING VALUES ===")
pct_missing = (df.isnull().sum() / len(df) * 100).round(2)
print(pct_missing)
print()

# Describe numeric columns
print("=== DESCRIBE (numeric columns) ===")
print(df.describe())
print()

# Unique countries
print("=== UNIQUE COUNTRIES ===")
print(df["countries"].unique().tolist())
print()

# Unique nutrition grades (excluding NaN for display)
print("=== UNIQUE NUTRITION GRADES ===")
grades = df["nutrition_grade"].dropna().unique().tolist()
print(sorted(grades))
print()

# Display products with missing nutrition grade
print("=== PRODUCTS WITH MISSING NUTRITION GRADE ===")
missing_grade = df[df["nutrition_grade"].isnull()]
print(missing_grade[["product_name", "nutrition_grade"]])
