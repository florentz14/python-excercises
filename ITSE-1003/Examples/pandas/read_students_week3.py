# -------------------------------------------------
# File Name: read_students_week3.py
# Created: 2026-04-18
# Author: Florentino Báez
# Description: Load students_week3.csv and display filtered subsets with tabulate.
# -------------------------------------------------

"""
Load students_week3.csv (Id column + student rows) with pandas.

Uses tabulate for nicer console tables (see requirements.txt: tabulate).

From repo root:
    python ITSE-1003/Examples/pandas/read_students_week3.py
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from tabulate import tabulate

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
CSV_PATH = DATA_DIR / "students_week3.csv"

COLUMNS_TO_SHOW = [
    "Id",
    "Name",
    "Major",
    "Grade",
    "Credits",
    "OnScholarship",
    "AttendancePct",
]

# tablefmt options: "github", "simple", "pretty", "grid", "fancy_grid", etc.
TABLE_FMT = "fancy_grid"


def show_df(frame: pd.DataFrame | pd.Series, title: str | None = None) -> None:
    """Print a DataFrame (or a one-row Series) as a plain-text table via tabulate."""
    if title:
        print(title)
    table = frame if isinstance(frame, pd.DataFrame) else frame.to_frame().T
    print(tabulate(table, headers="keys", tablefmt=TABLE_FMT, showindex=False))
    print()


def main() -> None:
    df = pd.read_csv(CSV_PATH)
   
    # step 1: print the shape of the dataframe
    print("Shape (rows, columns):", df.shape, "\n")

    # step 2: print the first 5 rows of the dataframe
    show_df(df.head(), "First rows:")

    # step 3: print the row where Id == 1
    show_df(df.loc[df["Id"] == 1], "Row where Id == 1:")

    # step 4: print the students with Grade >= 90
    show_df(df.loc[df["Grade"] >= 90, COLUMNS_TO_SHOW], "Students with Grade >= 90:")


if __name__ == "__main__":
    main()
