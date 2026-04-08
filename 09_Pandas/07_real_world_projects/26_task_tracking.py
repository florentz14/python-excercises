# -------------------------------------------------
# File Name: 52_task_tracking.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pending by assignee, delays, completed tasks analysis.
# -------------------------------------------------

"""
Task Tracking Analyzer
Answers: who has most pending, which project has most delays, tasks closed this month
"""

import pandas as pd
from pathlib import Path

CSV_PATH = Path(__file__).parent.parent / "data" / "tasks.csv"


def main():
    df = pd.read_csv(CSV_PATH)
    df["created"] = pd.to_datetime(df["created"])
    df["completed"] = pd.to_datetime(df["completed"], errors="coerce")
    df["due_date"] = pd.to_datetime(df["due_date"])

    print("[1] Load & Explore")
    print("-" * 50)
    print(f"Tasks: {len(df)}")

    # Tasks by status
    print("\n[2] Tasks by status:")
    print(df["status"].value_counts().to_string())

    # Most pending by assignee
    pending = df[df["status"] == "pending"]
    by_assignee = pd.DataFrame(
        pending.groupby("assignee", as_index=False).agg(task_count=("task_name", "size"))
    )
    by_assignee_rows = sorted(
        by_assignee.itertuples(index=False),
        key=lambda row: int(row[1]),
        reverse=True,
    )
    by_assignee = pd.DataFrame(by_assignee_rows, columns=["assignee", "task_count"])
    print("\n[3] Most pending tasks by assignee:")
    print(by_assignee.set_index("assignee")["task_count"].to_string())

    # Delayed (in_progress or pending, past due)
    today = pd.Timestamp("2024-01-15")  # simulate current date
    open_tasks = pd.DataFrame(df[df["status"].isin(["in_progress", "pending"])])
    delayed = pd.DataFrame(open_tasks[open_tasks["due_date"] < today])
    print("\n[4] Delayed tasks (past due):")
    if len(delayed) > 0:
        delayed_df = pd.DataFrame(delayed.loc[:, ["task_name", "assignee", "due_date", "status"]])
        print(delayed_df.to_string(index=False))
    else:
        print("  None")

    # Delays by project
    if len(delayed) > 0:
        print("\n[5] Delays by project:")
        delayed_projects = pd.Series(delayed["project"])
        print(delayed_projects.value_counts().to_string())

    # Completed this month
    completed = pd.DataFrame(df[df["status"] == "completed"]).dropna(subset=["completed"])
    jan_completed = completed[completed["completed"].dt.month == 1]
    print(f"\n[6] Tasks completed in January: {len(jan_completed)}")


if __name__ == "__main__":
    main()
