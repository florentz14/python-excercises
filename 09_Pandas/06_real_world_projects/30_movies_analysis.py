# -------------------------------------------------
# File Name: 56_movies_analysis.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Best genre, releases by year, top 10 movies.
# -------------------------------------------------

"""
Movies/Series Analyzer
Answers: genre with best avg rating, year with most releases, top 10
"""

import pandas as pd
from pathlib import Path

CSV_PATH = Path(__file__).parent.parent / "data" / "movies.csv"


def main():
    df = pd.read_csv(CSV_PATH)

    print("[1] Load & Explore")
    print("-" * 50)
    print(f"Titles: {len(df)}")

    # Genre with best average rating
    by_genre = df.groupby("genre")["rating"].agg(["mean", "count"])
    by_genre = by_genre.sort_values("mean", ascending=False)
    print("\n[2] Average rating by genre:")
    print(by_genre.to_string())

    best_genre = by_genre["mean"].idxmax()
    print(f"\n[3] Best-rated genre: {best_genre} (avg {by_genre.loc[best_genre, 'mean']:.1f})")

    # Year with most releases
    by_year = df.groupby("year").size().sort_values(ascending=False)
    print("\n[4] Releases by year:")
    print(by_year.to_string())

    # Top 10 by rating
    top10 = df.nlargest(10, "rating")[["title", "genre", "year", "rating"]]
    print("\n[5] Top 10 by rating:")
    print(top10.to_string(index=False))

    # By platform
    print("\n[6] Titles by platform:")
    print(df["platform"].value_counts().to_string())


if __name__ == "__main__":
    main()
