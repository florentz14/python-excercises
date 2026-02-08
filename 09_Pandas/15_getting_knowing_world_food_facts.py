# -------------------------------------------------
# File Name: 15_getting_knowing_world_food_facts.py
# Author: Florentino Báez
# Date: Pandas
# Description: Explore the World Food Facts Dataset. Load food product data
#              with nutrition info. Use info(), describe(), columns, and
#              isnull() to understand data quality.
# -------------------------------------------------

import pandas as pd
import numpy as np

# Create sample food product data with some NaN values (no external CSV)
food_data = {
    "product_name": [
        "Organic Whole Milk",
        "Dark Chocolate Bar",
        "Greek Yogurt",
        "Whole Grain Bread",
        "Orange Juice",
        "Cheddar Cheese",
        "Peanut Butter",
        "Tomato Ketchup",
        "Corn Flakes",
        "Salmon Fillet",
        "Honey",
        "Olive Oil",
    ],
    "brands": [
        "FarmFresh",
        "CocoaDeluxe",
        "YogurtCo",
        "BakeryBest",
        np.nan,
        "CheeseMaster",
        "NutSpread",
        "SauceCo",
        "CerealCo",
        np.nan,
        "BeeNatural",
        "MediterraneanOil",
    ],
    "categories": [
        "Dairy",
        "Snacks",
        "Dairy",
        "Bakery",
        "Beverages",
        "Dairy",
        "Spreads",
        "Condiments",
        "Cereals",
        "Seafood",
        "Sweeteners",
        "Oils",
    ],
    "countries": [
        "United States",
        "Belgium",
        "Greece",
        "Germany",
        "United States",
        "United Kingdom",
        "United States",
        "Netherlands",
        "United Kingdom",
        "Norway",
        "Spain",
        "Italy",
    ],
    "energy_100g": [266.0, 546.0, 97.0, 246.0, 45.0, 402.0, 598.0, 112.0, 376.0, np.nan, 304.0, 884.0],
    "fat_100g": [3.3, 31.0, 0.7, 3.2, 0.2, 33.0, 50.0, 0.1, 0.9, 13.0, 0.0, 100.0],
    "carbohydrates_100g": [4.8, 56.0, 3.6, 49.0, 10.4, 1.3, 20.0, 27.0, 84.0, 0.0, 82.0, 0.0],
    "proteins_100g": [3.2, 5.5, 9.0, 9.0, 0.7, 25.0, 25.0, 1.8, 7.0, 20.0, 0.3, 0.0],
    "salt_100g": [0.1, 0.02, 0.04, 1.1, np.nan, 1.8, 0.6, 2.7, 0.7, 0.1, 0.0, 0.0],
    "nutrition_grade": [
        "b",
        "d",
        "a",
        "b",
        "c",
        "d",
        "d",
        "d",
        np.nan,
        "a",
        "c",
        np.nan,
    ],
}

df = pd.DataFrame(food_data)

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
