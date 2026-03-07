# -------------------------------------------------
# File Name: 15_employees_avg_salary.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Horizontal Bar — Average Salary by Department (Top 10).
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

# Group by department, calculate mean salary, sort descending, take top 10
avg_salary = (df.groupby("department_name")["salary"]
                .mean()
                .sort_values(ascending=True)  # Ascending so highest appears at top of horizontal chart
                .tail(10))

plt.figure(figsize=(9, 6))
colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(avg_salary)))  # Gradient colors from viridis colormap
bars = plt.barh(avg_salary.index, avg_salary.values, color=colors, edgecolor="black", linewidth=0.5)

# Add value labels at the end of each bar
for bar, val in zip(bars, avg_salary.values):
    plt.text(bar.get_width() + 200, bar.get_y() + bar.get_height() / 2,
             f"${val:,.0f}", va="center", fontsize=9, fontweight="bold")

plt.title("Top 10 Departments by Average Salary", fontsize=14, fontweight="bold")
plt.xlabel("Average Salary (USD)")
plt.grid(axis="x", alpha=0.3)  # Vertical grid lines only for salary comparison
plt.tight_layout()
plt.show()
