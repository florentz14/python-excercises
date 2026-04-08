import pandas as pd


employees = pd.DataFrame(
    {"name": ["Alice", "Bob", "Carol"], "department": ["HR", "IT", "Finance"]},
    index=[101, 102, 103],
)
salaries = pd.DataFrame({"salary": [70000, 90000, 85000]}, index=[101, 102, 103])
extra = pd.DataFrame({"bonus": [5000, 7000]}, index=[101, 104])
dept_info = pd.DataFrame({"location": ["Building A", "Building B", "Building C"]}, index=[101, 102, 103])

print("employees.join(salaries):")
print(employees.join(salaries))
print("\nemployees.join(extra, how='left'):")
print(employees.join(extra, how="left"))
print("\nemployees.join(extra, how='outer'):")
print(employees.join(extra, how="outer"))
print("\nemployees.join([salaries, dept_info]):")
print(employees.join([salaries, dept_info]))
