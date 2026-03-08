# -------------------------------------------------
# File Name: 13_lunch_analysis.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Analyzes student performance by lunch type (socioeconomic indicator).
# -------------------------------------------------

"""
Lunch Type Analysis (Socioeconomic Indicator)
Examines how lunch type (standard vs free/reduced) affects performance
"""

import pandas as pd
import numpy as np


def lunch_analysis(csv_file):
    """Analyzes the impact of lunch type on student performance."""
    df = pd.read_csv(csv_file)
    df["average_score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)

    print("=" * 80)
    print("LUNCH TYPE ANALYSIS (SOCIOECONOMIC INDICATOR)")
    print("=" * 80)

    # Distribution
    print("\n[STUDENT DISTRIBUTION]")
    print("-" * 80)
    distribution = df["lunch"].value_counts()
    for lunch_type, count in distribution.items():
        pct = (count / len(df)) * 100
        print(f"{lunch_type.capitalize():15}: {count:3d} students ({pct:.2f}%)")

    # Comparative averages
    print("\n\n[GRADE COMPARISON BY LUNCH TYPE]")
    print("-" * 80)
    print(f"{'Lunch Type':15} {'Math':>12} {'Reading':>12} {'Writing':>12} {'Average':>12}")
    print("-" * 80)

    results = {}
    for lunch_type in df["lunch"].unique():
        df_type = df[df["lunch"] == lunch_type]
        math_avg = df_type["math score"].mean()
        reading_avg = df_type["reading score"].mean()
        writing_avg = df_type["writing score"].mean()
        total_avg = df_type["average_score"].mean()

        results[lunch_type] = {
            "math": math_avg,
            "reading": reading_avg,
            "writing": writing_avg,
            "total": total_avg,
            "count": len(df_type),
        }
        print(f"{lunch_type.capitalize():15} {math_avg:12.2f} {reading_avg:12.2f} {writing_avg:12.2f} {total_avg:12.2f}")

    # Performance gap
    print("\n\n[PERFORMANCE GAP]")
    print("-" * 80)
    if "standard" in results and "free/reduced" in results:
        gap_math = results["standard"]["math"] - results["free/reduced"]["math"]
        gap_reading = results["standard"]["reading"] - results["free/reduced"]["reading"]
        gap_writing = results["standard"]["writing"] - results["free/reduced"]["writing"]
        gap_total = results["standard"]["total"] - results["free/reduced"]["total"]

        print("Difference (Standard - Free/Reduced):")
        print(f"  Math:    {gap_math:+.2f} points")
        print(f"  Reading: {gap_reading:+.2f} points")
        print(f"  Writing: {gap_writing:+.2f} points")
        print(f"  Average: {gap_total:+.2f} points")
        pct_gap = (gap_total / results["free/reduced"]["total"]) * 100
        print(f"\n  → Percentage gap: {pct_gap:.2f}%")

    # Grade distribution
    print("\n\n[GRADE DISTRIBUTION]")
    print("-" * 80)
    ranges = [(0, 60, "Low"), (60, 75, "Medium"), (75, 90, "High"), (90, 100, "Excellent")]

    for lunch_type in df["lunch"].unique():
        df_type = df[df["lunch"] == lunch_type]
        print(f"\n{lunch_type.capitalize()}:")
        for min_val, max_val, category in ranges:
            count = ((df_type["average_score"] >= min_val) & (df_type["average_score"] < max_val)).sum()
            pct = (count / len(df_type)) * 100
            print(f"  {category:12} ({min_val:2d}-{max_val:2d}): {count:3d} students ({pct:5.2f}%)")

    # Gender and lunch analysis
    print("\n\n[GENDER AND LUNCH TYPE ANALYSIS]")
    print("-" * 80)
    for gender in df["gender"].unique():
        print(f"\n{gender.capitalize()}:")
        df_gender = df[df["gender"] == gender]
        for lunch_type in df["lunch"].unique():
            df_combined = df_gender[df_gender["lunch"] == lunch_type]
            if len(df_combined) > 0:
                avg = df_combined["average_score"].mean()
                print(f"  {lunch_type.capitalize():15}: {avg:6.2f} points ({len(df_combined):3d} students)")

    # Top students
    print("\n\n[STUDENTS WITH AVERAGE >= 85]")
    print("-" * 80)
    for lunch_type in df["lunch"].unique():
        df_type = df[df["lunch"] == lunch_type]
        count_high = (df_type["average_score"] >= 85).sum()
        pct = (count_high / len(df_type)) * 100
        print(f"{lunch_type.capitalize():15}: {count_high:3d} students ({pct:5.2f}%)")

    # Test preparation and lunch
    print("\n\n[INTERACTION: TEST PREPARATION AND LUNCH TYPE]")
    print("-" * 80)
    for lunch_type in df["lunch"].unique():
        print(f"\n{lunch_type.capitalize()}:")
        df_lunch = df[df["lunch"] == lunch_type]
        for prep in df["test preparation course"].unique():
            df_combined = df_lunch[df_lunch["test preparation course"] == prep]
            if len(df_combined) > 0:
                avg = df_combined["average_score"].mean()
                print(f"  Prep {prep:10}: {avg:6.2f} points ({len(df_combined):3d} students)")

    # Variability
    print("\n\n[VARIABILITY (Standard Deviation)]")
    print("-" * 80)
    for lunch_type in df["lunch"].unique():
        df_type = df[df["lunch"] == lunch_type]
        std = df_type["average_score"].std()
        print(f"{lunch_type.capitalize():15}: {std:.2f}")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    from pathlib import Path

    csv_path = Path(__file__).parent / "data" / "StudentsPerformance.csv"
    lunch_analysis(csv_path)
