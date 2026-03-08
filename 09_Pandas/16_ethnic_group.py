# -------------------------------------------------
# File Name: 16_ethnic_group.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Analyzes student performance by ethnic group.
# -------------------------------------------------

"""
Ethnic Group Performance Analysis
Examines performance differences between ethnic groups
"""

import pandas as pd
import numpy as np


def ethnic_group_analysis(csv_file):
    """Analyzes academic performance by ethnic group."""
    df = pd.read_csv(csv_file)
    df["average_score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)

    print("=" * 90)
    print("PERFORMANCE BY ETHNIC GROUP")
    print("=" * 90)

    # Distribution
    print("\n[ETHNIC GROUP DISTRIBUTION]")
    print("-" * 90)
    distribution = df["race/ethnicity"].value_counts().sort_index()
    for group, count in distribution.items():
        pct = (count / len(df)) * 100
        print(f"{group:15}: {count:3d} students ({pct:.2f}%)")

    # Averages by group
    print("\n\n[AVERAGE SCORES BY ETHNIC GROUP]")
    print("-" * 90)
    print(f"{'Group':15} {'Math':>12} {'Reading':>12} {'Writing':>12} {'Average':>12} {'N':>8}")
    print("-" * 90)

    results = []
    for group in sorted(df["race/ethnicity"].unique()):
        df_group = df[df["race/ethnicity"] == group]
        r = {
            "group": group,
            "math": df_group["math score"].mean(),
            "reading": df_group["reading score"].mean(),
            "writing": df_group["writing score"].mean(),
            "total": df_group["average_score"].mean(),
            "count": len(df_group),
        }
        results.append(r)
        print(f"{group:15} {r['math']:12.2f} {r['reading']:12.2f} {r['writing']:12.2f} {r['total']:12.2f} {r['count']:8d}")

    # Ranking
    print("\n\n🏆 RANKING BY AVERAGE PERFORMANCE")
    print("-" * 90)
    sorted_results = sorted(results, key=lambda x: x["total"], reverse=True)
    for i, r in enumerate(sorted_results, 1):
        print(f"{i}. {r['group']:15} - {r['total']:.2f} points")

    # Gap analysis
    print("\n\n[PERFORMANCE GAPS]")
    print("-" * 90)
    best = sorted_results[0]
    worst = sorted_results[-1]
    print(f"Best group:   {best['group']:15} ({best['total']:.2f})")
    print(f"Worst group: {worst['group']:15} ({worst['total']:.2f})")
    print(f"Total gap:   {best['total'] - worst['total']:.2f} points")
    print(f"\nGaps by subject:")
    print(f"  Math:    {best['math'] - worst['math']:.2f} points")
    print(f"  Reading: {best['reading'] - worst['reading']:.2f} points")
    print(f"  Writing: {best['writing'] - worst['writing']:.2f} points")

    # Top performers
    print("\n\n[STUDENTS WITH AVERAGE >= 85 BY GROUP]")
    print("-" * 90)
    for group in sorted(df["race/ethnicity"].unique()):
        df_group = df[df["race/ethnicity"] == group]
        count_high = (df_group["average_score"] >= 85).sum()
        pct = (count_high / len(df_group)) * 100
        print(f"{group:15}: {count_high:3d} students ({pct:5.2f}%)")

    # Grade distribution
    print("\n\n[PERFORMANCE DISTRIBUTION BY GROUP]")
    print("-" * 90)
    ranges = [(0, 60, "Low"), (60, 75, "Medium"), (75, 90, "High"), (90, 100, "Excellent")]
    for group in sorted(df["race/ethnicity"].unique()):
        df_group = df[df["race/ethnicity"] == group]
        print(f"\n{group}:")
        for min_val, max_val, category in ranges:
            count = ((df_group["average_score"] >= min_val) & (df_group["average_score"] < max_val)).sum()
            pct = (count / len(df_group)) * 100
            print(f"  {category:12} ({min_val:2d}-{max_val:2d}): {count:3d} students ({pct:5.2f}%)")

    # Parental education interaction
    print("\n\n[ETHNIC GROUP AND PARENTAL EDUCATION]")
    print("-" * 90)
    college_levels = ["some college", "associate's degree", "bachelor's degree", "master's degree"]
    for group in sorted(df["race/ethnicity"].unique()):
        df_group = df[df["race/ethnicity"] == group]
        count_college = df_group[df_group["parental level of education"].isin(college_levels)].shape[0]
        pct = (count_college / len(df_group)) * 100
        avg_college = df_group[df_group["parental level of education"].isin(college_levels)]["average_score"].mean()
        print(f"{group:15}: {pct:5.2f}% with college education (average: {avg_college:.2f})")

    # Gender by group
    print("\n\n[AVERAGE BY ETHNIC GROUP AND GENDER]")
    print("-" * 90)
    for group in sorted(df["race/ethnicity"].unique()):
        print(f"\n{group}:")
        df_group = df[df["race/ethnicity"] == group]
        for gender in df["gender"].unique():
            df_combined = df_group[df_group["gender"] == gender]
            if len(df_combined) > 0:
                avg = df_combined["average_score"].mean()
                print(f"  {gender.capitalize():8}: {avg:6.2f} points ({len(df_combined):3d} students)")

    print("\n" + "=" * 90)


if __name__ == "__main__":
    from pathlib import Path

    csv_path = Path(__file__).parent / "data" / "StudentsPerformance.csv"
    ethnic_group_analysis(csv_path)
