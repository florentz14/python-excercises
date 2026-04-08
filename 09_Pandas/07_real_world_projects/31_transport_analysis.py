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

CSV_PATH = Path(__file__).parent.parent / "data" / "transport.csv"


def main():
    df = pd.read_csv(CSV_PATH)
    df["date"] = pd.to_datetime(df["date"])

    print("[1] Load & Explore")
    print("-" * 50)
    print(f"Trips: {len(df)}")

    # Average duration per route
    by_route = pd.DataFrame(
        df.groupby("route", as_index=False).agg(
            duration_min=("duration_min", "mean"),
            distance_km=("distance_km", "first"),
            cost=("cost", "mean"),
        )
    ).round(1)
    by_route_rows = sorted(
        by_route.itertuples(index=False),
        key=lambda row: float(row[1]),
        reverse=True,
    )
    by_route = pd.DataFrame(
        by_route_rows, columns=["route", "duration_min", "distance_km", "cost"]
    )
    print("\n[2] Avg duration (min) by route:")
    print(by_route.set_index("route")["duration_min"].to_string())

    longest_row = by_route.iloc[0]
    print(
        f"\n[3] Longest route (avg time): {longest_row['route']} "
        f"({float(longest_row['duration_min']):.0f} min)"
    )

    # Driver with most trips
    by_driver = df["driver_id"].value_counts()
    print("\n[4] Trips by driver:")
    print(by_driver.to_string())

    # Day with most delays
    delayed = df[df["delay_min"] > 0]
    if len(delayed) > 0:
        by_date = pd.DataFrame(
            delayed.groupby("date", as_index=False).agg(total_delay=("delay_min", "sum"))
        )
        by_date_rows = sorted(
            by_date.itertuples(index=False),
            key=lambda row: float(row[1]),
            reverse=True,
        )
        by_date = pd.DataFrame(by_date_rows, columns=["date", "total_delay"])
        worst_day_row = by_date.iloc[0]
        worst_day_ts = pd.Timestamp(worst_day_row["date"])
        print(
            f"\n[5] Day with most delays: {worst_day_ts.date()} "
            f"(total {float(worst_day_row['total_delay']):.0f} min)"
        )

    # Total cost
    print(f"\n[6] Total cost: ${df['cost'].sum():,.2f}")


if __name__ == "__main__":
    main()
