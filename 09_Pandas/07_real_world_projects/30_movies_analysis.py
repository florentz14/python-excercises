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
    by_genre = pd.DataFrame(
        df.groupby("genre", as_index=False).agg(
            mean_rating=("rating", "mean"),
            rating_count=("rating", "count"),
        )
    )
    by_genre_rows = sorted(
        by_genre.itertuples(index=False),
        key=lambda row: float(row[1]),
        reverse=True,
    )
    by_genre = pd.DataFrame(by_genre_rows, columns=["genre", "mean_rating", "rating_count"])
    print("\n[2] Average rating by genre:")
    print(by_genre.set_index("genre").to_string())

    best_genre_row = by_genre.iloc[0]
    print(f"\n[3] Best-rated genre: {best_genre_row['genre']} (avg {float(best_genre_row['mean_rating']):.1f})")

    # Year with most releases
    by_year = pd.DataFrame(df.groupby("year", as_index=False).agg(release_count=("title", "size")))
    by_year_rows = sorted(
        by_year.itertuples(index=False),
        key=lambda row: int(row[1]),
        reverse=True,
    )
    by_year = pd.DataFrame(by_year_rows, columns=["year", "release_count"])
    print("\n[4] Releases by year:")
    print(by_year.set_index("year")["release_count"].to_string())

    # Top 10 by rating
    top10 = df.nlargest(10, "rating")[["title", "genre", "year", "rating"]]
    print("\n[5] Top 10 by rating:")
    print(top10.to_string(index=False))

    # By platform
    print("\n[6] Titles by platform:")
    print(df["platform"].value_counts().to_string())


if __name__ == "__main__":
    main()
