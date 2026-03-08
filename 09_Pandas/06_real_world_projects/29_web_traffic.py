# -------------------------------------------------
# File Name: 55_web_traffic.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Top pages, traffic by day, conversion by source.
# -------------------------------------------------

"""
Web Traffic Analyzer
Answers: most visited page, day with most traffic, best converting source
"""

import pandas as pd
from pathlib import Path

CSV_PATH = Path(__file__).parent.parent / "data" / "web_traffic.csv"


def main():
    df = pd.read_csv(CSV_PATH)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["date"] = df["timestamp"].dt.date
    df["day_of_week"] = df["timestamp"].dt.day_name()

    print("[1] Load & Explore")
    print("-" * 50)
    print(f"Page views: {len(df)}, Sessions: {df['session_id'].nunique()}")

    # Most visited page
    by_page = df["page"].value_counts()
    print("\n[2] Most visited pages:")
    print(by_page.to_string())

    # Day with most traffic
    by_date = df.groupby("date").size().sort_values(ascending=False)
    best_day = by_date.idxmax()
    print(f"\n[3] Day with most traffic: {best_day} ({by_date[best_day]} views)")

    # Best converting source
    sessions_with_conv = df[df["converted"] == 1]["session_id"].unique()
    df_session = df.groupby("session_id").agg({"source": "first", "converted": "max"}).reset_index()
    by_source = df_session.groupby("source").agg(total_sessions=("session_id", "count"), conversions=("converted", "sum"))
    by_source["conv_rate"] = (by_source["conversions"] / by_source["total_sessions"] * 100).round(1)
    print("\n[4] Conversion rate by source:")
    print(by_source.to_string())

    # Page views per session
    views_per_session = df.groupby("session_id").size()
    print(f"\n[5] Avg page views per session: {views_per_session.mean():.1f}")


if __name__ == "__main__":
    main()
