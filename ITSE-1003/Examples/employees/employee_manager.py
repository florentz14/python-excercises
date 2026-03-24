# -------------------------------------------------
# File Name: ITSE-1003/Examples/employees/employee_manager.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Employee manager logic.
# -------------------------------------------------

import sys
from pathlib import Path

_examples_dir = Path(__file__).resolve().parent.parent
if str(_examples_dir) not in sys.path:
    sys.path.append(str(_examples_dir))

from utils import *
from employee_model import *


class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        print('Enter employee data')
        name = input("Enter employee name")
        age = input_int("Enter employee age: ")
        salary = input_float("Enter employee salary: ")
        emp_id = len(self.employees) + 1
        department = input("Enter employee department: ")
        position = input("Enter employee position: ")
        self.employees.append(Employee(emp_id, name, age, salary, department, position))

    def list_employee(self):
        if len(self.employees) == 0:
            print("\nEmployee list is empty !")
            return
        else:
            for emp in self.employees:
                print(emp)

    def delete_employees_with_age(self, age_from, age_to):
        for emp in self.employees:
            if age_from <= emp.age <= age_to:
                print(f"\tDeleting employee {emp.name}")
                self.employees.remove(emp)

    def find_employee_by_name(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def update_salary_by_name(self, name, salary):
        emp = self.find_employee_by_name(name)
        if emp is None:
            print('Error: No employee found')
        else:
            emp.salary = salary