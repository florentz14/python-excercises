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
    by_message = errors["message"].value_counts()
    print("\n[2] Most frequent errors:")
    print(by_message.head(5).to_string())

    # Hour with most failures
    failures = df[df["level"].isin(["ERROR", "WARNING"])]
    by_hour = failures.groupby("hour").size().sort_values(ascending=False)
    print("\n[3] Hour with most failures:")
    peak_hour = by_hour.idxmax()
    print(f"  Hour {peak_hour}:00 - {by_hour[peak_hour]} events")

    # Server with most warnings
    warnings = df[df["level"] == "WARNING"]
    by_server = warnings["server"].value_counts()
    print("\n[4] Server with most warnings:")
    print(by_server.to_string())

    # Events by level
    print("\n[5] Events by level:")
    print(df["level"].value_counts().to_string())


if __name__ == "__main__":
    main()
