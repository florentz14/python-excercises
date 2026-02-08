# -------------------------------------------------
# File Name: 18_employees_salary_box.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Box Plot — Salary Distribution by Department (Top 6).
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

# Count employees per department
dept_counts = df["department_name"].value_counts()

# Get the 6 departments with the most employees
top_6_depts = dept_counts.head(6).index.tolist()

# Filter data for those departments only
filtered = df[df["department_name"].isin(top_6_depts)]

# Create a list of salary arrays, one per department (for boxplot)
box_data = [filtered[filtered["department_name"] == d]["salary"].dropna().values
            for d in top_6_depts]

fig, ax = plt.subplots(figsize=(10, 6))
bp = ax.boxplot(box_data, labels=top_6_depts, patch_artist=True,  # patch_artist fills boxes with color
                notch=True,  # Notch shows confidence interval around the median
                medianprops=dict(color="black", linewidth=2))

# Color each box differently
box_colors = plt.cm.Pastel1(np.linspace(0, 0.8, len(top_6_depts)))
for patch, color in zip(bp["boxes"], box_colors):
    patch.set_facecolor(color)

ax.set_title("Salary Distribution by Department (Top 6)", fontsize=14, fontweight="bold")
ax.set_ylabel("Salary (USD)")
ax.set_xlabel("Department")
ax.grid(axis="y", alpha=0.3)  # Horizontal grid for salary comparison
plt.xticks(rotation=30, ha="right")  # Rotate labels if names are long
plt.tight_layout()
plt.show()
