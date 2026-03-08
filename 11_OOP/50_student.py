# -------------------------------------------------
# File Name: 50_student.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Simple Student class with name, grade, __str__ and passed().
# -------------------------------------------------

class Student:
    """Class with attributes and __str__."""
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name} - Grade: {self.grade}"

    def passed(self):
        return self.grade >= 60

# Short list of students
students = [
    Student("Alice", 85),
    Student("Bob", 52),
    Student("Carol", 91),
]

# Usage
for s in students:
    status = "Passed" if s.passed() else "Failed"
    print(f"{s} [{status}]")
