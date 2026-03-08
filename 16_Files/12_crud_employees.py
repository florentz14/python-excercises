# -------------------------------------------------
# File Name: 12_crud_employees.py
# Author: Florentino Báez
# Date: 16_Files
# Description: CRUD operations on employee data file. Create, read, update, delete.
# -------------------------------------------------

import json
from pathlib import Path

# Data file path (same folder as this script)
FOLDER = Path(__file__).parent
DATA_FILE = FOLDER / "employees.json"


def load_employees() -> list[dict]:
    """Reads the JSON file and returns the employee list. Returns [] if it does not exist."""
    if not DATA_FILE.is_file():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_employees(employees: list[dict]) -> None:
    """Saves the employee list to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(employees, f, indent=2, ensure_ascii=False)


def generate_id(employees: list[dict]) -> int:
    """Returns the next available ID (current max + 1)."""
    if not employees:
        return 1
    return max(e["id"] for e in employees) + 1


def display_employee(e: dict) -> None:
    """Prints a formatted employee."""
    print(f"  ID: {e['id']}")
    print(f"  Name: {e['name']}")
    print(f"  Position: {e['position']}")
    print(f"  Department: {e['department']}")
    print(f"  Salary: {e['salary']}")
    print(f"  Email: {e['email']}")


# --- CREATE ---
def create_employee(employees: list[dict]) -> list[dict]:
    """Prompts for data, creates an employee and adds to the list. Returns updated list."""
    print("\n--- Create employee ---")
    name = input("Name: ").strip()
    position = input("Position: ").strip()
    department = input("Department: ").strip()
    try:
        salary = float(input("Salary: ").strip().replace(",", "."))
    except ValueError:
        salary = 0.0
    email = input("Email: ").strip()

    new_emp = {
        "id": generate_id(employees),
        "name": name,
        "position": position,
        "department": department,
        "salary": salary,
        "email": email,
    }
    employees.append(new_emp)
    save_employees(employees)
    print(f"Employee created with ID {new_emp['id']}.")
    return employees


# --- LIST ---
def list_employees(employees: list[dict]) -> None:
    """Displays all employees."""
    print("\n--- Employee list ---")
    if not employees:
        print("No employees registered.")
        return
    for e in employees:
        display_employee(e)
        print("-" * 40)


# --- SEARCH BY ID ---
def find_by_id(employees: list[dict], search_id: int) -> dict | None:
    """Returns the employee with that ID or None."""
    for e in employees:
        if e["id"] == search_id:
            return e
    return None


# --- EDIT ---
def edit_employee(employees: list[dict]) -> list[dict]:
    """Prompts for ID, modifies the fields the user specifies and saves."""
    print("\n--- Edit employee ---")
    if not employees:
        print("No employees to edit.")
        return employees
    try:
        edit_id = int(input("ID of employee to edit: ").strip())
    except ValueError:
        print("Invalid ID.")
        return employees

    emp = find_by_id(employees, edit_id)
    if not emp:
        print(f"No employee with ID {edit_id} exists.")
        return employees

    print("Leave blank to keep current value.")
    name = input(f"New name [{emp['name']}]: ").strip()
    position = input(f"New position [{emp['position']}]: ").strip()
    department = input(f"New department [{emp['department']}]: ").strip()
    salary_str = input(f"New salary [{emp['salary']}]: ").strip()
    email = input(f"New email [{emp['email']}]: ").strip()

    if name:
        emp["name"] = name
    if position:
        emp["position"] = position
    if department:
        emp["department"] = department
    if salary_str:
        try:
            emp["salary"] = float(salary_str.replace(",", "."))
        except ValueError:
            pass
    if email:
        emp["email"] = email

    save_employees(employees)
    print("Employee updated.")
    return employees


# --- DELETE RECORD ---
def delete_record(employees: list[dict]) -> list[dict]:
    """Prompts for ID, removes that employee from the list and saves the file."""
    print("\n--- Delete record ---")
    if not employees:
        print("No employees to delete.")
        return employees
    try:
        delete_id = int(input("ID of employee to delete: ").strip())
    except ValueError:
        print("Invalid ID.")
        return employees

    emp = find_by_id(employees, delete_id)
    if not emp:
        print(f"No employee with ID {delete_id} exists.")
        return employees

    confirm = input(f"Delete {emp['name']}? (y/n): ").strip().lower()
    if confirm == "y":
        employees = [e for e in employees if e["id"] != delete_id]
        save_employees(employees)
        print("Record deleted.")
    else:
        print("Operation cancelled.")
    return employees


# --- DELETE FILE ---
def delete_file(employees: list[dict]) -> list[dict]:
    """Deletes the data file and returns an empty list."""
    print("\n--- Delete data file ---")
    if not DATA_FILE.exists():
        print("Data file does not exist.")
        return []
    confirm = input("Delete file and all records? (y/n): ").strip().lower()
    if confirm == "y":
        DATA_FILE.unlink()
        print("File deleted. Employee list is now empty.")
        return []
    print("Operation cancelled.")
    return employees


def view_one(employees: list[dict]) -> None:
    """Displays one employee by ID."""
    print("\n--- View employee by ID ---")
    if not employees:
        print("No employees registered.")
        return
    try:
        view_id = int(input("Employee ID: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    emp = find_by_id(employees, view_id)
    if emp:
        display_employee(emp)
    else:
        print(f"No employee with ID {view_id} exists.")


def menu() -> None:
    """Main CRUD menu."""
    employees = load_employees()

    while True:
        print("\n" + "=" * 50)
        print("  CRUD EMPLOYEES (file: employees.json)")
        print("=" * 50)
        print("  1. Create employee")
        print("  2. List all employees")
        print("  3. View employee by ID")
        print("  4. Edit employee")
        print("  5. Delete record (one employee)")
        print("  6. Delete file (remove all data)")
        print("  0. Exit")
        print("=" * 50)
        option = input("Option: ").strip()

        if option == "1":
            employees = create_employee(employees)
        elif option == "2":
            list_employees(employees)
        elif option == "3":
            view_one(employees)
        elif option == "4":
            employees = edit_employee(employees)
        elif option == "5":
            employees = delete_record(employees)
        elif option == "6":
            employees = delete_file(employees)
        elif option == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()
