# -------------------------------------------------
# File Name: 16_employees_salary_hist.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Histogram — Salary Distribution with Mean and Median Lines.
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

# Load CSV files from the 09_Pandas folder
pandas_dir = Path(__file__).parent.parent / "09_Pandas"  # Navigate one level up, then into 09_Pandas
# Read employees and departments CSVs
employees = pd.read_csv(pandas_dir / "employees.csv")
departments = pd.read_csv(pandas_dir / "departments.csv")
# Merge to get department names alongside salaries
df = pd.merge(employees, departments, on="department_id", how="left")  # Left join keeps all employees

plt.figure(figsize=(8, 5))
# Plot histogram of all employee salaries
plt.hist(df["salary"].dropna(), bins=20, color="steelblue", edgecolor="black", alpha=0.8)

# Add a vertical line for the median salary
median_sal = df["salary"].median()
plt.axvline(median_sal, color="red", linestyle="--", linewidth=2, label=f"Median: ${median_sal:,.0f}")

# Add a vertical line for the mean salary
mean_sal = df["salary"].mean()
plt.axvline(mean_sal, color="orange", linestyle="-.", linewidth=2, label=f"Mean: ${mean_sal:,.0f}")

plt.title("Salary Distribution Across All Employees", fontsize=14, fontweight="bold")
plt.xlabel("Salary (USD)")
plt.ylabel("Number of Employees")
plt.legend(fontsize=11)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
