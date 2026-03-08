# -------------------------------------------------
# File Name: 57_transport_analysis.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Longest route, trips by driver, delay analysis.
# -------------------------------------------------

"""
Transport Analyzer
Answers: longest route, driver with most trips, day with most delays
"""

import pandas as pd
from pathlib import Path

CSV_PATH = Path(__file__).parent / "data" / "transport.csv"


def main():
    df = pd.read_csv(CSV_PATH)
    df["date"] = pd.to_datetime(df["date"])

    print("[1] Load & Explore")
    print("-" * 50)
    print(f"Trips: {len(df)}")

    # Average duration per route
    by_route = df.groupby("route").agg({
        "duration_min": "mean",
        "distance_km": "first",
        "cost": "mean"
    }).round(1)
    by_route = by_route.sort_values("duration_min", ascending=False)
    print("\n[2] Avg duration (min) by route:")
    print(by_route["duration_min"].to_string())

    longest = by_route["duration_min"].idxmax()
    print(f"\n[3] Longest route (avg time): {longest} ({by_route.loc[longest, 'duration_min']:.0f} min)")

    # Driver with most trips
    by_driver = df["driver_id"].value_counts()
    print("\n[4] Trips by driver:")
    print(by_driver.to_string())

    # Day with most delays
    delayed = df[df["delay_min"] > 0]
    if len(delayed) > 0:
        by_date = delayed.groupby("date")["delay_min"].sum()
        worst_day = by_date.idxmax()
        print(f"\n[5] Day with most delays: {worst_day.date()} (total {by_date[worst_day]:.0f} min)")

    # Total cost
    print(f"\n[6] Total cost: ${df['cost'].sum():,.2f}")


if __name__ == "__main__":
    main()
