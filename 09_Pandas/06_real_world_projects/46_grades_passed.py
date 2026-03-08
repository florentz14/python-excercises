# -------------------------------------------------
# File Name: 92_grades_passed.py
# Author: Florentino Báez
# Date: Pandas
# Description: Passing grades sorted descending.
# -------------------------------------------------

import pandas as pd


def grades_passed(grades_dict: dict, passing: float = 5.0) -> pd.Series:
    """Receives dict {student: grade} and returns Series of passing grades sorted."""
    s = pd.Series(grades_dict)
    return s[s >= passing].sort_values(ascending=False)


if __name__ == "__main__":
    grades = {"Anna": 8.5, "Luis": 6.0, "Maria": 9.2, "Peter": 5.5, "Sara": 7.8, "John": 4.2}
    passed = grades_passed(grades)
    print("Passing grades (>= 5) sorted:")
    print(passed)
