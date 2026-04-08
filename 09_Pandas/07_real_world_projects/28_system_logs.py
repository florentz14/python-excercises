# -------------------------------------------------
# File Name: 54_system_logs.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Most errors, peak hour, server warnings from log data.
# -------------------------------------------------

"""
System Logs Analyzer
Answers: most frequent error, hour with most failures, server with most warnings
"""

import pandas as pd
from pathlib import Path

CSV_PATH = Path(__file__).parent.parent / "data" / "system_logs.csv"


def main():
    df = pd.read_csv(CSV_PATH)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["hour"] = df["timestamp"].dt.hour
    df["date"] = df["timestamp"].dt.date

    print("[1] Load & Explore")
    print("-" * 50)
    print(f"Log entries: {len(df)}")

    # Most frequent error type (by message pattern)
    errors = df[df["level"] == "ERROR"]
    by_message = pd.Series(errors["message"]).value_counts()
    print("\n[2] Most frequent errors:")
    print(by_message.head(5).to_string())

    # Hour with most failures
    failures = df[df["level"].isin(["ERROR", "WARNING"])]
    by_hour = pd.DataFrame(
        failures.groupby("hour", as_index=False).agg(event_count=("hour", "size"))
    )
    by_hour_rows = sorted(
        by_hour.itertuples(index=False),
        key=lambda row: int(row[1]),
        reverse=True,
    )
    by_hour = pd.DataFrame(by_hour_rows, columns=["hour", "event_count"])
    print("\n[3] Hour with most failures:")
    peak_hour_row = by_hour.iloc[0]
    print(f"  Hour {int(peak_hour_row['hour'])}:00 - {int(peak_hour_row['event_count'])} events")

    # Server with most warnings
    warnings = df[df["level"] == "WARNING"]
    by_server = pd.Series(warnings["server"]).value_counts()
    print("\n[4] Server with most warnings:")
    print(by_server.to_string())

    # Events by level
    print("\n[5] Events by level:")
    print(pd.Series(df["level"]).value_counts().to_string())


if __name__ == "__main__":
    main()
