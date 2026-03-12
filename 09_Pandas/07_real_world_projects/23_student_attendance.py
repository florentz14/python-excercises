# -------------------------------------------------
# File Name: 49_student_attendance.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Analyzes absences, attendance %, at-risk students.
# -------------------------------------------------

"""
Student Attendance Analyzer
Answers: who missed most, which group has best attendance, students under 80%
"""

import pandas as pd
from pathlib import Path

CSV_PATH = Path(__file__).parent.parent / "data" / "student_attendance.csv"


def load_and_clean(df):
    """Clean duplicates, parse dates."""
    df = df.drop_duplicates(subset=["date", "student_id"])
    df["date"] = pd.to_datetime(df["date"])
    return df


def analyze(df):
    """Answer attendance questions."""
    print("[1] Load & Explore")
    print("-" * 50)
    print(f"Records: {len(df)}, Dates: {df['date'].nunique()}")

    # Who missed the most
    absences = df[df["status"] == "absent"].groupby("student_id").size()
    absences = absences.sort_values(ascending=False)
    print("\n[2] Most absences:")
    for sid, cnt in absences.head(5).items():
        name = df[df["student_id"] == sid]["student_name"].iloc[0]
        print(f"  {name} ({sid}): {cnt} absences")

    # Attendance % by group
    total_days = df["date"].nunique()
    by_group = df[df["status"] == "present"].groupby("group")["student_id"].count()
    group_sizes = df.groupby("group")["student_id"].nunique() * total_days
    pct = (by_group / group_sizes * 100).round(1)
    print("\n[3] Attendance % by group:")
    print(pct.to_string())

    # Students under 80%
    present_count = df[df["status"] == "present"].groupby("student_id").size()
    expected = total_days
    pct_per_student = (present_count / expected * 100)
    at_risk = pct_per_student[pct_per_student < 80]
    print("\n[4] Students with attendance < 80%:")
    for sid in at_risk.index:
        name = df[df["student_id"] == sid]["student_name"].iloc[0]
        print(f"  {name}: {pct_per_student[sid]:.1f}%")


def main():
    df = pd.read_csv(CSV_PATH)
    df = load_and_clean(df)
    analyze(df)


if __name__ == "__main__":
    main()
