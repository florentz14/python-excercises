# -------------------------------------------------
# File Name: 17_employees_dept_pie.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Pie Chart — Employee Distribution by Department.
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

# Keep top 8 departments, group the rest into "Other"
top_8 = dept_counts.head(8)
other = dept_counts.iloc[8:].sum()  # Sum of all remaining departments
if other > 0:
    top_8["Other"] = other  # Append "Other" category

# Custom colors for each slice
pie_colors = plt.cm.Set3(np.linspace(0, 1, len(top_8)))  # Set3 colormap gives pastel tones

plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(
    top_8.values,
    labels=top_8.index,
    autopct="%1.1f%%",       # Show percentage with one decimal
    colors=pie_colors,
    startangle=140,           # Rotate so first slice starts at ~upper-left
    pctdistance=0.8,          # Distance of % label from center
    textprops={"fontsize": 10}
)

# Style the percentage labels
for autotext in autotexts:
    autotext.set_fontweight("bold")

plt.title("Employee Distribution by Department", fontsize=14, fontweight="bold", pad=20)
plt.axis("equal")  # Equal aspect ratio ensures a perfect circle
plt.tight_layout()
plt.show()
