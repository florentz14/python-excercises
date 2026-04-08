# -------------------------------------------------
# File Name: 58_hr_analysis.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Headcount by dept, salary stats, top earners, hires by year.
# -------------------------------------------------

from pathlib import Path

import pandas as pd

DATA = Path(__file__).parent.parent / "data"
emp = pd.read_csv(DATA / "employees.csv", parse_dates=["hire_date"])
dept = pd.read_csv(DATA / "departments.csv")
jobs = pd.read_csv(DATA / "jobs.csv")

# Merge employees with departments and jobs
df = emp.merge(dept[["department_id", "department_name"]], on="department_id", how="left")
df = df.merge(jobs[["job_id", "job_title"]], on="job_id", how="left")

print("=== HEADCOUNT BY DEPARTMENT ===")
headcount = pd.DataFrame(
    df.groupby("department_name", as_index=False).agg(employee_count=("employee_id", "size"))
)
headcount_rows = sorted(
    headcount.itertuples(index=False),
    key=lambda row: int(row[1]),
    reverse=True,
)
headcount = pd.DataFrame(headcount_rows, columns=["department_name", "employee_count"])
print(headcount.set_index("department_name")["employee_count"].to_string())
print()

print("=== AVG SALARY BY DEPARTMENT ===")
print(df.groupby("department_name")["salary"].agg(["mean", "min", "max", "count"]))
print()

print("=== TOP 5 EARNERS ===")
top = df.nlargest(5, "salary")[["first_name", "last_name", "job_title", "department_name", "salary"]]
print(top.to_string(index=False))
print()

print("=== EMPLOYEES BY JOB TITLE ===")
print(df["job_title"].value_counts().head(10))
print()

print("=== HIRES BY YEAR ===")
df["hire_year"] = df["hire_date"].dt.year
print(df.groupby("hire_year").size())
