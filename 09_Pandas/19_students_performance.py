# -------------------------------------------------
# File Name: 19_students_performance.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Full CSV analysis: load, stats, averages for student performance.
# -------------------------------------------------

"""
StudentsPerformance.csv Analysis
Loads the CSV, summarizes statistics and analyzes scores by gender,
lunch, test preparation, and parental education level.
"""

import pandas as pd
from pathlib import Path

CSV_PATH = Path(__file__).parent / "data" / "StudentsPerformance.csv"


def load_data() -> pd.DataFrame:
    """Loads the CSV and converts score columns to numeric."""
    df = pd.read_csv(CSV_PATH, encoding="utf-8")
    for col in ["math score", "reading score", "writing score"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def general_summary(df: pd.DataFrame) -> None:
    """Shows dimensions, columns, types and descriptive statistics."""
    print("=" * 60)
    print("GENERAL SUMMARY")
    print("=" * 60)
    print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
    print("\nColumns:", list(df.columns))
    print("\nTypes:\n", df.dtypes)
    print("\nDescriptive statistics (scores):")
    score_cols = [c for c in df.columns if "score" in c]
    if score_cols:
        print(df[score_cols].describe().to_string())
    print("\nMissing values per column:")
    print(df.isna().sum().to_string())


def averages_by_category(df: pd.DataFrame) -> None:
    """Average scores by gender, lunch, preparation and parental education."""
    score_cols = [c for c in df.columns if "score" in c]
    if not score_cols:
        return

    print("\n" + "=" * 60)
    print("AVERAGES BY CATEGORY")
    print("=" * 60)

    if "gender" in df.columns:
        print("\n--- By gender ---")
        print(df.groupby("gender")[score_cols].mean().round(2).to_string())

    if "lunch" in df.columns:
        print("\n--- By lunch type ---")
        print(df.groupby("lunch")[score_cols].mean().round(2).to_string())

    col_prep = "test preparation course"
    if col_prep in df.columns:
        print("\n--- By test preparation ---")
        print(df.groupby(col_prep)[score_cols].mean().round(2).to_string())

    col_edu = "parental level of education"
    if col_edu in df.columns:
        print("\n--- By parental education level ---")
        print(df.groupby(col_edu)[score_cols].mean().round(2).to_string())


def global_average_score(df: pd.DataFrame) -> None:
    """Creates 'average score' column and shows summary."""
    score_cols = [c for c in df.columns if "score" in c]
    if not score_cols:
        return
    df["average score"] = df[score_cols].mean(axis=1)
    print("\n" + "=" * 60)
    print("GLOBAL AVERAGE SCORE (math, reading, writing)")
    print("=" * 60)
    print(df["average score"].describe().to_string())


def main() -> None:
    if not CSV_PATH.is_file():
        print(f"File not found: {CSV_PATH}")
        return

    df = load_data()
    general_summary(df)
    averages_by_category(df)
    global_average_score(df)
    print("\n" + "=" * 60)
    print("Analysis complete.")
    print("=" * 60)


if __name__ == "__main__":
    main()
