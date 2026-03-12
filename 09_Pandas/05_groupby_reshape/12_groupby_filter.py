# -------------------------------------------------
# File Name: 72_groupby_filter.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: GroupBy combined with filter.
# -------------------------------------------------

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "dept": ["Sales", "Sales", "IT", "IT", "IT", "HR"],
    "emp": ["A", "B", "C", "D", "E", "F"],
    "salary": [30, 40, 50, 60, 70, 45],
})

print("=== ORIGINAL ===")
print(df)
print()

# filter — keep groups that satisfy condition
# Keep only depts with avg salary > 45
filtered = df.groupby("dept").filter(lambda g: g["salary"].mean() > 45)
print("=== filter: mean(salary) > 45 ===")
print(filtered)
print()

# Keep depts with at least 3 employees
filtered2 = df.groupby("dept").filter(lambda g: len(g) >= 3)
print("=== filter: len >= 3 ===")
print(filtered2)
print()

# filter + transform: flag rows in "large" depts
dept_size = df.groupby("dept")["emp"].transform("count")
df["in_large_dept"] = dept_size >= 3
print("=== Rows in depts with >= 3 employees ===")
print(df[df["in_large_dept"]])
