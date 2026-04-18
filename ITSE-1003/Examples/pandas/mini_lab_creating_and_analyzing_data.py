"""
Mini Lab - Creating and Analyzing Data with Pandas

Objective: build a dataset from a Python dictionary, convert it to a DataFrame,
and perform basic exploration, selection, filtering, and new columns.

Run (from repo root):
    python ITSE-1003/Examples/pandas/mini_lab_creating_and_analyzing_data.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    # Part 1 — Create the Dictionary
    mydata = {
        "Student": ["Ana", "Luis", "Marta", "John"],
        "Hours_Studied": [5, 3, 8, 2],
        "Score": [80, 60, 90, 50],
    }

    # Part 2 — Convert to DataFrame
    df = pd.DataFrame(mydata)
    print("Part 2 - DataFrame")
    print(df)
    print()

    # Part 3 — Explore the Data
    print("Part 3 - head()")
    print(df.head())
    print()
    print("Part 3 - info()")
    df.info()
    print()

    # Part 4 — Select Data
    print('Part 4 - column "Student"')
    print(df["Student"])
    print()
    print("Part 4 - columns Student, Score")
    print(df[["Student", "Score"]])
    print()

    # Part 5 — Filter Data
    print("Part 5 - Hours_Studied > 4")
    print(df[df["Hours_Studied"] > 4])
    print()

    # Part 6 — Create a New Column
    df["Status"] = df["Score"] > 70
    print("Part 6 - Status (Score > 70)")
    print(df)
    print()

    # Challenge Questions
    print("Challenge 1 - Who has the highest score?")
    top = df[df["Score"] == df["Score"].max()]
    print(top[["Student", "Score"]])
    print()

    print("Challenge 2 - Sort by score (highest to lowest)")
    print(df.sort_values(by="Score", ascending=False))


if __name__ == "__main__":
    main()
