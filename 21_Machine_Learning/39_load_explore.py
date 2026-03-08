# -------------------------------------------------
# File Name: 39_load_explore.py
# Author: Florentino Báez
# Date: 21_Machine_Learning
# Description: Load and explore data with pandas.
# -------------------------------------------------

import pandas as pd
import os

# Path to data (relative to this script)
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "09_Pandas", "data")


def load_and_explore(filename, description):
    """Load a CSV and display basic information."""
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        print(f"⚠️  File not found: {path}")
        return None

    df = pd.read_csv(path)
    print("=" * 60)
    print(f"  {description}")
    print("=" * 60)
    print(f"\nDimensions: {df.shape[0]} rows x {df.shape[1]} columns")
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nInfo (types and nulls):")
    print(df.info())
    print("\nNumeric statistics:")
    print(df.describe())
    print("\nNull values per column:")
    print(df.isnull().sum())
    print()
    return df


# --- Dataset 1: Iris (classification) ---
df_iris = load_and_explore("iris.csv", "IRIS - Flower species classification")

# --- Dataset 2: Students (regression) ---
df_students = load_and_explore(
    "StudentsPerformance.csv",
    "STUDENTS - Math, reading and writing scores"
)

print("[OK] Step 1 completed. You can now load and explore data with pandas.")
