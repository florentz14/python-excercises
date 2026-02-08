"""
Exercise 3: Nested Dictionaries
This exercise demonstrates how to work with dictionaries inside dictionaries.
Nested dictionaries are useful for representing hierarchical data structures.
"""

def main():
    print("Exercise 3: Nested Dictionaries")
    print("=" * 60)
    
    # Creating a nested dictionary - company employees
    company = {
        "engineering": {
            "manager": {
                "name": "John Smith",
                "salary": 95000,
                "experience": 8
            },
            "developers": [
                {"name": "Alice Chen", "salary": 75000, "language": "Python"},
                {"name": "Bob Wilson", "salary": 72000, "language": "Java"}
            ]
        },
        "sales": {
            "manager": {
                "name": "Sarah Davis",
                "salary": 90000,
                "experience": 6
            },
            "representatives": [
                {"name": "Mike Brown", "salary": 55000, "region": "East"},
                {"name": "Lisa Johnson", "salary": 58000, "region": "West"}
            ]
        }
    }
    
    print("1. Accessing Nested Dictionary Values:")
    print("-" * 60)
    # Access engineering manager's name
    eng_manager = company["engineering"]["manager"]["name"]
    print(f"Engineering Manager: {eng_manager}")
    
    # Access first developer
    first_dev = company["engineering"]["developers"][0]["name"]
    print(f"First Developer: {first_dev}")
    print()
    
    print("2. Iterating Through Nested Dictionaries:")
    print("-" * 60)
    for department, dept_data in company.items():
        print(f"\n{department.upper()} Department:")
        print(f"  Manager: {dept_data['manager']['name']}")
        print(f"  Manager Salary: ${dept_data['manager']['salary']:,}")
    print()
    
    print("3. Modifying Nested Values:")
    print("-" * 60)
    # Give engineering manager a raise
    old_salary = company["engineering"]["manager"]["salary"]
    company["engineering"]["manager"]["salary"] = 100000
    new_salary = company["engineering"]["manager"]["salary"]
    print(f"Engineering Manager raise:")
    print(f"  Old: ${old_salary:,}")
    print(f"  New: ${new_salary:,}")
    print()
    
    print("4. Adding to Nested Structures:")
    print("-" * 60)
    # Add new developer
    new_developer = {
        "name": "Charlie Parker",
        "salary": 78000,
        "language": "JavaScript"
    }
    company["engineering"]["developers"].append(new_developer)
    print(f"Added new developer: {new_developer['name']}")
    print(f"Total developers: {len(company['engineering']['developers'])}")
    print()
    
    print("5. Creating a Summary Report:")
    print("-" * 60)
    for dept_name, dept_info in company.items():
        total_employees = 1  # manager
        if "developers" in dept_info:
            total_employees += len(dept_info["developers"])
        elif "representatives" in dept_info:
            total_employees += len(dept_info["representatives"])
        
        print(f"{dept_name.capitalize()}: {total_employees} employees")
    print()
    
    # Creating a more complex nested structure - school database
    print("6. Complex Nested Example - School Database:")
    print("-" * 60)
    school = {
        "grade_10": {
            "class_A": {
                "teacher": "Mr. Anderson",
                "students": {
                    "student_001": {"name": "Emma", "grade": 92},
                    "student_002": {"name": "Noah", "grade": 88}
                }
            },
            "class_B": {
                "teacher": "Ms. Taylor",
                "students": {
                    "student_003": {"name": "Olivia", "grade": 95},
                    "student_004": {"name": "Liam", "grade": 90}
                }
            }
        }
    }
    
    # Access deeply nested value
    emma_grade = school["grade_10"]["class_A"]["students"]["student_001"]["grade"]
    print(f"Emma's grade: {emma_grade}")
    
    # Calculate average for a class
    class_a_students = school["grade_10"]["class_A"]["students"]
    grades = [student["grade"] for student in class_a_students.values()]
    avg_grade = sum(grades) / len(grades)
    print(f"Class A average: {avg_grade:.1f}")
    
    print("\n" + "=" * 60)
    print("Best Practices for Nested Dictionaries:")
    print("  - Keep nesting levels reasonable (max 3-4)")
    print("  - Use clear, descriptive key names")
    print("  - Consider using classes for very complex structures")
    print("  - Use .get() for safer access to avoid KeyErrors")
    print("  - Document the structure for team members")


if __name__ == "__main__":
    main()
