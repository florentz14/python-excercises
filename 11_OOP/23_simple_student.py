# 23_simple_student.py - Simple class: Student
# Florentino Baez - ITSE-1002

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
