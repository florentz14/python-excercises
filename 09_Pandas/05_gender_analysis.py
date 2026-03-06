# ------------------------------------------------------------
# File: 05_gender_analysis.py
# Purpose: Gender Performance Analysis.
# Description: Compares male vs female performance, per-subject gaps,
#              high-score distribution, standard deviation.
# ------------------------------------------------------------

"""
Gender Performance Analysis
Compares academic performance between male and female students
"""

import pandas as pd
import numpy as np


def gender_analysis(csv_file):
    """Analyzes academic performance by gender."""
    df = pd.read_csv(csv_file)
    df["average_score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)

    print("=" * 80)
    print("PERFORMANCE BY GENDER")
    print("=" * 80)

    # Distribution
    print("\n[STUDENT DISTRIBUTION]")
    print("-" * 80)
    distribution = df["gender"].value_counts()
    for gender, count in distribution.items():
        pct = (count / len(df)) * 100
        print(f"{gender.capitalize():8}: {count:3d} students ({pct:.2f}%)")

    # Averages
    print("\n\n[AVERAGE SCORES BY GENDER]")
    print("-" * 80)
    print(f"{'':15} {'Math':>12} {'Reading':>12} {'Writing':>12} {'Average':>12}")
    print("-" * 80)
    for gender in df["gender"].unique():
        df_g = df[df["gender"] == gender]
        math_avg = df_g["math score"].mean()
        reading_avg = df_g["reading score"].mean()
        writing_avg = df_g["writing score"].mean()
        total_avg = df_g["average_score"].mean()
        print(f"{gender.capitalize():15} {math_avg:12.2f} {reading_avg:12.2f} {writing_avg:12.2f} {total_avg:12.2f}")

    # Gender differences
    print("\n\n[GENDER DIFFERENCES]")
    print("-" * 80)
    male_math = df[df["gender"] == "male"]["math score"].mean()
    female_math = df[df["gender"] == "female"]["math score"].mean()
    male_reading = df[df["gender"] == "male"]["reading score"].mean()
    female_reading = df[df["gender"] == "female"]["reading score"].mean()
    male_writing = df[df["gender"] == "male"]["writing score"].mean()
    female_writing = df[df["gender"] == "female"]["writing score"].mean()

    diff_math = male_math - female_math
    diff_reading = male_reading - female_reading
    diff_writing = male_writing - female_writing

    print(f"Math:    {'Males' if diff_math > 0 else 'Females'} lead by {abs(diff_math):.2f} points")
    print(f"Reading: {'Males' if diff_reading > 0 else 'Females'} lead by {abs(diff_reading):.2f} points")
    print(f"Writing: {'Males' if diff_writing > 0 else 'Females'} lead by {abs(diff_writing):.2f} points")

    # Top performers
    print("\n\n🏆 STUDENTS WITH EXCELLENT SCORES (≥85)")
    print("-" * 80)
    for subject in ["math score", "reading score", "writing score"]:
        print(f"\n{subject.replace(' score', '').capitalize()}:")
        for gender in df["gender"].unique():
            df_g = df[df["gender"] == gender]
            count_high = (df_g[subject] >= 85).sum()
            pct = (count_high / len(df_g)) * 100
            print(f"  {gender.capitalize():8}: {count_high:3d} students ({pct:5.2f}%)")

    # Variability
    print("\n\n[VARIABILITY (Standard Deviation)]")
    print("-" * 80)
    print(f"{'':15} {'Math':>12} {'Reading':>12} {'Writing':>12}")
    print("-" * 80)
    for gender in df["gender"].unique():
        df_g = df[df["gender"] == gender]
        math_std = df_g["math score"].std()
        reading_std = df_g["reading score"].std()
        writing_std = df_g["writing score"].std()
        print(f"{gender.capitalize():15} {math_std:12.2f} {reading_std:12.2f} {writing_std:12.2f}")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    from pathlib import Path

    csv_path = Path(__file__).parent / "data" / "StudentsPerformance.csv"
    gender_analysis(csv_path)
