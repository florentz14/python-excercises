# ------------------------------------------------------------
# File: 03_general_analysis.py
# Purpose: General Student Performance Analysis.
# Description: Descriptive stats, averages per subject, grade distribution,
#              best/worst students, correlation matrix.
# ------------------------------------------------------------

"""
General Student Performance Analysis
Provides overall descriptive statistics of the dataset
"""

import pandas as pd
import numpy as np


def general_analysis(csv_file):
    """Performs a general statistical analysis of the dataset."""
    df = pd.read_csv(csv_file)

    print("=" * 80)
    print("GENERAL STUDENT PERFORMANCE ANALYSIS")
    print("=" * 80)

    # Dataset info
    print("\n[DATASET INFORMATION]")
    print("-" * 80)
    print(f"Total students: {len(df)}")
    print(f"Number of columns: {len(df.columns)}")
    print(f"\nAvailable columns:")
    for col in df.columns:
        print(f"  - {col}")

    # Descriptive stats
    print("\n\n[DESCRIPTIVE STATISTICS (SCORES)]")
    print("-" * 80)
    scores = df[["math score", "reading score", "writing score"]]
    print(scores.describe())

    # Averages per subject
    print("\n\n[AVERAGE BY SUBJECT]")
    print("-" * 80)
    print(f"Math:    {df['math score'].mean():.2f}")
    print(f"Reading: {df['reading score'].mean():.2f}")
    print(f"Writing: {df['writing score'].mean():.2f}")
    df["average_score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)
    print(f"\nOverall average: {df['average_score'].mean():.2f}")

    # Grade distribution
    print("\n\n[GRADE DISTRIBUTION]")
    print("-" * 80)
    ranges = [(0, 50, "Low"), (50, 70, "Medium"), (70, 85, "High"), (85, 100, "Excellent")]
    for subject in ["math score", "reading score", "writing score"]:
        print(f"\n{subject.replace(' score', '').capitalize()}:")
        for min_val, max_val, category in ranges:
            count = ((df[subject] >= min_val) & (df[subject] < max_val)).sum()
            pct = (count / len(df)) * 100
            print(f"  {category:12} ({min_val:2d}-{max_val:2d}): {count:3d} students ({pct:5.2f}%)")

    # Top / bottom students
    print("\n\n[TOP AND BOTTOM PERFORMERS]")
    print("-" * 80)
    best_idx = df["average_score"].idxmax()
    worst_idx = df["average_score"].idxmin()
    print("Best student:")
    print(f"  Average: {df.loc[best_idx, 'average_score']:.2f}")
    print(f"  Math: {df.loc[best_idx, 'math score']}, Reading: {df.loc[best_idx, 'reading score']}, Writing: {df.loc[best_idx, 'writing score']}")
    print("\nStudent with most difficulties:")
    print(f"  Average: {df.loc[worst_idx, 'average_score']:.2f}")
    print(f"  Math: {df.loc[worst_idx, 'math score']}, Reading: {df.loc[worst_idx, 'reading score']}, Writing: {df.loc[worst_idx, 'writing score']}")

    # Correlation
    print("\n\n[CORRELATION BETWEEN SUBJECTS]")
    print("-" * 80)
    print(scores.corr())

    print("\n" + "=" * 80)


if __name__ == "__main__":
    from pathlib import Path

    csv_path = Path(__file__).parent / "data" / "StudentsPerformance.csv"
    general_analysis(csv_path)
