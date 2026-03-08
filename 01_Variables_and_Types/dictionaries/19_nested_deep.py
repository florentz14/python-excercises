# -------------------------------------------------
# File Name: 19_nested_deep.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Deeply nested dicts (3+ levels) with chained key access.
# -------------------------------------------------

company = {
    "engineering": {
        "emp001": {"name": "Alice", "role": "Developer", "salary": 80000},
        "emp002": {"name": "Bob", "role": "Architect", "salary": 95000},
    },
    "sales": {
        "emp003": {"name": "Carol", "role": "Manager", "salary": 75000},
    }
}

print("Deeply Nested Dictionary (3 levels)")
print("-" * 40)

# Access: company -> department -> employee -> field
print("Alice's role:", company["engineering"]["emp001"]["role"])
print("Carol's salary:", company["sales"]["emp003"]["salary"])

# Iterate departments, then employees
print("\nAll employees by department:")
for dept, employees in company.items():
    print(f"  {dept}:")
    for emp_id, info in employees.items():
        print(f"    {emp_id}: {info['name']} - {info['role']}")
