# -------------------------------------------------
# File Name: 91_grades_stats.py
# Author: Florentino Báez
# Date: Pandas
# Description: Grade statistics: min, max, mean, std.
# -------------------------------------------------

import pandas as pd


def grade_stats(grades_dict: dict) -> pd.Series:
    """Receives dict {student: grade} and returns Series with statistics."""
    s = pd.Series(grades_dict)
    return pd.Series({
        "min": s.min(),
        "max": s.max(),
        "mean": s.mean(),
        "std": s.std(),
    })


if __name__ == "__main__":
    grades = {"Anna": 8.5, "Luis": 6.0, "Maria": 9.2, "Peter": 5.5, "Sara": 7.8}
    result = grade_stats(grades)
    print("Grade statistics:")
    print(result)
