# -------------------------------------------------
# File Name: 02_employees_pay.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Professor: Mauricio Quiroga
# Date: Module 06 Lab
# Description: Employees Pay Program. Megan owns a small neighborhood coffee
#              shop with six employees who work as baristas. All employees
#              have the same hourly pay rate. The program allows entering the
#              number of hours worked by each employee and displays the
#              amounts of all employees' gross pay. Steps:
#              1. For each employee: get the number of hours worked and store
#                 it in a list element.
#              2. For each list element: use the value to calculate an
#                 employee's gross pay and display the amount.
# -------------------------------------------------

# =============================================================================
# EXERCISE 2: Employees Pay Program
# =============================================================================

print("=" * 60)
print("EXERCISE 2: Employees Pay Program")
print("=" * 60)

# Constants
NUM_EMPLOYEES = 6  # Number of employees
HOURLY_PAY_RATE = 15.00  # Hourly pay rate (same for all employees)

# Initialize list to store hours worked
hours_worked = []

# Get hours worked for each employee
# Try-except block: Handles exceptions that may occur during input conversion
try:
    print(f"Enter hours worked for {NUM_EMPLOYEES} employees:")
    print(f"Hourly pay rate: ${HOURLY_PAY_RATE:.2f}")

    # Loop (for): Iterates for each employee to collect hours worked
    for employee in range(1, NUM_EMPLOYEES + 1):
        while True:
            # Loop (while True): Continuously prompts until valid hours are provided
            try:
                hours = float(
                    input(f"  Enter hours worked for employee {employee}: "))
                if hours < 0:
                    print(
                        "    Error: Hours worked cannot be negative. Please try again.")
                    continue  # Continue loop to ask for input again
                hours_worked.append(hours)  # Add hours to the list
                break  # Exit the while loop when valid input is processed
            except ValueError:
                # Handle invalid numeric input (e.g., non-numeric characters)
                print("    Error: Please enter a valid number.")

    # Calculate and display gross pay for each employee
    print("\n" + "=" * 60)
    print("EMPLOYEE GROSS PAY REPORT")
    print("=" * 60)
    print(f"Hourly Pay Rate: ${HOURLY_PAY_RATE:.2f}")
    print(f"\nEmployee\tHours Worked\tGross Pay")
    print("-" * 50)

    # Loop (for): Iterates through each employee to calculate and display gross pay
    for i in range(len(hours_worked)):
        gross_pay = hours_worked[i] * HOURLY_PAY_RATE  # Calculate gross pay
        print(f"Employee {i + 1}\t{hours_worked[i]:.2f}\t\t${gross_pay:.2f}")

    # Calculate and display totals
    total_hours = sum(hours_worked)  # Calculate total hours worked
    total_gross_pay = total_hours * HOURLY_PAY_RATE  # Calculate total gross pay
    print("-" * 50)
    print(f"Total\t\t{total_hours:.2f}\t\t${total_gross_pay:.2f}")

except Exception as e:
    # Handle any other unexpected errors
    print(f"Error: {e}")

print()

# =============================================================================
# CITATIONS
# =============================================================================
# 1. List Operations in Python:
#    - List methods: append()
#    - sum() function for totaling list values
#    Source: Python Documentation - Built-in Functions
#    https://docs.python.org/3/library/functions.html
#
# 2. Payroll Calculation:
#    - Gross Pay = Hours Worked × Hourly Rate
#    Source: Standard payroll calculation formula
