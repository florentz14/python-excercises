# -------------------------------------------------
# File Name: 19_nested_dictionaries.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Nested Dictionaries.
#              Shows how to work with dictionaries inside
#              dictionaries. Includes accessing nested values,
#              iterating, modifying, and a complex school
#              database example with grade calculations.
# -------------------------------------------------

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
    # Access nested values using chained bracket notation
    # Each level of nesting requires another set of brackets
    eng_manager = company["engineering"]["manager"]["name"]
    print(f"Engineering Manager: {eng_manager}")
    
    # Access nested list within dictionary, then dictionary within list
    # First index [0] gets first developer dict, then ["name"] gets the name
    first_dev = company["engineering"]["developers"][0]["name"]
    print(f"First Developer: {first_dev}")
    print()
    
    print("2. Iterating Through Nested Dictionaries:")
    print("-" * 60)
    # Iterate through top-level keys (departments) and their nested values
    # dept_data contains the nested dictionary for each department
    for department, dept_data in company.items():
        print(f"\n{department.upper()} Department:")
        # Access nested values through the dept_data dictionary
        print(f"  Manager: {dept_data['manager']['name']}")
        print(f"  Manager Salary: ${dept_data['manager']['salary']:,}")
    print()
    
    print("3. Modifying Nested Values:")
    print("-" * 60)
    # Modify nested values using the same chained bracket notation
    # Store old value before modification for comparison
    old_salary = company["engineering"]["manager"]["salary"]
    company["engineering"]["manager"]["salary"] = 100000
    new_salary = company["engineering"]["manager"]["salary"]
    print(f"Engineering Manager raise:")
    print(f"  Old: ${old_salary:,}")
    print(f"  New: ${new_salary:,}")
    print()
    
    print("4. Adding to Nested Structures:")
    print("-" * 60)
    # Add new items to nested lists within dictionaries
    # Create a new dictionary and append it to the nested list
    new_developer = {
        "name": "Charlie Parker",
        "salary": 78000,
        "language": "JavaScript"
    }
    # Access the nested list and use list.append() method
    company["engineering"]["developers"].append(new_developer)
    print(f"Added new developer: {new_developer['name']}")
    print(f"Total developers: {len(company['engineering']['developers'])}")
    print()
    
    print("5. Creating a Summary Report:")
    print("-" * 60)
    # Calculate totals by checking which nested keys exist
    # Different departments may have different nested structures
    for dept_name, dept_info in company.items():
        total_employees = 1  # Start with manager (always present)
        # Check for different employee types based on department structure
        if "developers" in dept_info:
            total_employees += len(dept_info["developers"])
        elif "representatives" in dept_info:
            total_employees += len(dept_info["representatives"])
        
        print(f"{dept_name.capitalize()}: {total_employees} employees")
    print()
    
    # Creating a more complex nested structure - school database
    # This demonstrates 4 levels of nesting: grade -> class -> students -> student info
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
    
    # Access deeply nested value using multiple bracket levels
    # Path: school -> grade_10 -> class_A -> students -> student_001 -> grade
    emma_grade = school["grade_10"]["class_A"]["students"]["student_001"]["grade"]
    print(f"Emma's grade: {emma_grade}")
    
    # Calculate average for a class
    # First, get the students dictionary for class A
    class_a_students = school["grade_10"]["class_A"]["students"]
    # Extract all grade values from student dictionaries using list comprehension
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
