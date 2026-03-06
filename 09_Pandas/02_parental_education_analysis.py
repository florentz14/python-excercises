# ------------------------------------------------------------
# File: 02_parental_education_analysis.py
# Purpose: Parental Education Level Analysis.
# Description: Examines how parental education impacts performance,
#              compares college vs non-college, ranks levels,
#              identifies high performers.
# ------------------------------------------------------------

"""
Parental Education Level Analysis
Examines how parental education level affects student performance
"""

import pandas as pd
import numpy as np


def parental_education_analysis(csv_file):
    """Analyzes the impact of parental education level on performance."""
    df = pd.read_csv(csv_file)
    df["average_score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)

    print("=" * 90)
    print("PERFORMANCE BY PARENTAL EDUCATION LEVEL")
    print("=" * 90)

    # Distribution
    print("\n[PARENTAL EDUCATION LEVEL DISTRIBUTION]")
    print("-" * 90)
    distribution = df["parental level of education"].value_counts().sort_values(ascending=False)
    for level, count in distribution.items():
        pct = (count / len(df)) * 100
        print(f"{level:25}: {count:3d} students ({pct:5.2f}%)")

    education_order = [
        "some high school",
        "high school",
        "some college",
        "associate's degree",
        "bachelor's degree",
        "master's degree",
    ]
    available_levels = [n for n in education_order if n in df["parental level of education"].unique()]

    # Averages by level
    print("\n\n[AVERAGE SCORES BY PARENTAL EDUCATION LEVEL]")
    print("-" * 90)
    print(f"{'Education Level':25} {'Math':>12} {'Reading':>12} {'Writing':>12} {'Average':>12}")
    print("-" * 90)

    results = []
    for level in available_levels:
        df_level = df[df["parental level of education"] == level]
        results.append({
            "level": level,
            "math": df_level["math score"].mean(),
            "reading": df_level["reading score"].mean(),
            "writing": df_level["writing score"].mean(),
            "total": df_level["average_score"].mean(),
        })
        r = results[-1]
        print(f"{level:25} {r['math']:12.2f} {r['reading']:12.2f} {r['writing']:12.2f} {r['total']:12.2f}")

    # Trend
    print("\n\n[TREND: EDUCATION LEVEL vs PERFORMANCE]")
    print("-" * 90)
    if len(results) >= 2:
        best = max(results, key=lambda x: x["total"])
        worst = min(results, key=lambda x: x["total"])
        print(f"Best average:   {best['level']:25} ({best['total']:.2f})")
        print(f"Lowest average: {worst['level']:25} ({worst['total']:.2f})")
        print(f"Difference:     {best['total'] - worst['total']:.2f} points")

    # College vs non-college
    print("\n\n[COMPARISON: COLLEGE vs NON-COLLEGE EDUCATION]")
    print("-" * 90)
    college = ["some college", "associate's degree", "bachelor's degree", "master's degree"]
    non_college = ["some high school", "high school"]

    df_college = df[df["parental level of education"].isin(college)]
    df_non = df[df["parental level of education"].isin(non_college)]

    if len(df_college) > 0 and len(df_non) > 0:
        print(f"\nCollege-educated parents ({len(df_college)} students):")
        print(f"  Average: {df_college['average_score'].mean():.2f}")
        print(f"  Math: {df_college['math score'].mean():.2f}, Reading: {df_college['reading score'].mean():.2f}, Writing: {df_college['writing score'].mean():.2f}")
        print(f"\nNon-college ({len(df_non)} students):")
        print(f"  Average: {df_non['average_score'].mean():.2f}")
        diff = df_college["average_score"].mean() - df_non["average_score"].mean()
        print(f"\n  → Difference in favor of college: {diff:.2f} points")

    # Top performers
    print("\n\n[STUDENTS WITH AVERAGE >= 80 BY EDUCATION LEVEL]")
    print("-" * 90)
    for level in available_levels:
        df_level = df[df["parental level of education"] == level]
        count_high = (df_level["average_score"] >= 80).sum()
        pct = (count_high / len(df_level)) * 100 if len(df_level) > 0 else 0
        print(f"{level:25}: {count_high:3d} students ({pct:5.2f}%)")

    print("\n" + "=" * 90)


if __name__ == "__main__":
    from pathlib import Path

    csv_path = Path(__file__).parent / "data" / "StudentsPerformance.csv"
    parental_education_analysis(csv_path)
