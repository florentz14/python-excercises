# ------------------------------------------------------------
# File: 06_test_preparation_analysis.py
# Purpose: Test Preparation Impact Analysis.
# Description: Evaluates how test prep affects scores: improvement per subject,
#              percentage gain, gender interaction, struggling students.
# ------------------------------------------------------------

"""
Test Preparation Impact Analysis
Evaluates how the test preparation course affects student performance
"""

import pandas as pd
import numpy as np


def test_preparation_analysis(csv_file):
    """Analyzes the impact of the test preparation course."""
    df = pd.read_csv(csv_file)
    df["average_score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)

    print("=" * 80)
    print("TEST PREPARATION IMPACT ANALYSIS")
    print("=" * 80)

    # Distribution
    print("\n[STUDENT DISTRIBUTION]")
    print("-" * 80)
    distribution = df["test preparation course"].value_counts()
    for status, count in distribution.items():
        pct = (count / len(df)) * 100
        print(f"{status.capitalize():15}: {count:3d} students ({pct:.2f}%)")

    # Averages
    print("\n\n📊 GRADE COMPARISON")
    print("-" * 80)
    print(f"{'Preparation':15} {'Math':>12} {'Reading':>12} {'Writing':>12} {'Average':>12}")
    print("-" * 80)

    results = {}
    for status in df["test preparation course"].unique():
        df_status = df[df["test preparation course"] == status]
        results[status] = {
            "math": df_status["math score"].mean(),
            "reading": df_status["reading score"].mean(),
            "writing": df_status["writing score"].mean(),
            "total": df_status["average_score"].mean(),
        }
        r = results[status]
        print(f"{status.capitalize():15} {r['math']:12.2f} {r['reading']:12.2f} {r['writing']:12.2f} {r['total']:12.2f}")

    # Impact
    print("\n\n[IMPACT OF PREPARATION]")
    print("-" * 80)
    if "completed" in results and "none" in results:
        imp_math = results["completed"]["math"] - results["none"]["math"]
        imp_reading = results["completed"]["reading"] - results["none"]["reading"]
        imp_writing = results["completed"]["writing"] - results["none"]["writing"]
        imp_total = results["completed"]["total"] - results["none"]["total"]

        print("Average improvement with preparation:")
        print(f"  Math:    {imp_math:+.2f} points")
        print(f"  Reading: {imp_reading:+.2f} points")
        print(f"  Writing: {imp_writing:+.2f} points")
        print(f"  Average: {imp_total:+.2f} points")
        pct_imp = (imp_total / results["none"]["total"]) * 100
        print(f"\n  → Percentage improvement: {pct_imp:+.2f}%")

    # Top performers
    print("\n\n[STUDENTS WITH EXCELLENT SCORES (>= 85)]")
    print("-" * 80)
    for status in df["test preparation course"].unique():
        df_status = df[df["test preparation course"] == status]
        print(f"\n{status.capitalize()}:")
        for subject in ["math score", "reading score", "writing score"]:
            count_high = (df_status[subject] >= 85).sum()
            pct = (count_high / len(df_status)) * 100
            print(f"  {subject.replace(' score', '').capitalize():12}: {count_high:3d} students ({pct:5.2f}%)")

    # Gender and preparation
    print("\n\n[PREPARATION IMPACT BY GENDER]")
    print("-" * 80)
    for gender in df["gender"].unique():
        print(f"\n{gender.capitalize()}:")
        df_g = df[df["gender"] == gender]
        for status in df["test preparation course"].unique():
            df_combined = df_g[df_g["test preparation course"] == status]
            if len(df_combined) > 0:
                avg = df_combined["average_score"].mean()
                print(f"  {status.capitalize():15}: {avg:6.2f} points ({len(df_combined):3d} students)")

    # Struggling students
    print("\n\n[STRUGGLING STUDENTS (Average < 60)]")
    print("-" * 80)
    for status in df["test preparation course"].unique():
        df_status = df[df["test preparation course"] == status]
        count_low = (df_status["average_score"] < 60).sum()
        pct = (count_low / len(df_status)) * 100
        print(f"{status.capitalize():15}: {count_low:3d} students ({pct:5.2f}%)")

    # Conclusion
    print("\n\n[CONCLUSION]")
    print("-" * 80)
    if "completed" in results and "none" in results:
        imp_total = results["completed"]["total"] - results["none"]["total"]
        if imp_total > 0:
            print(f"Test preparation shows a positive impact of {imp_total:.2f} points on average.")
            print("Encouraging participation in these courses is recommended.")
        else:
            print("Data does not show significant improvement from the preparation course.")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    from pathlib import Path

    csv_path = Path(__file__).parent / "data" / "StudentsPerformance.csv"
    test_preparation_analysis(csv_path)
