# -------------------------------------------------
# File Name: 55_grade_manager.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Student Grade Manager - CRUD operations, grade letters,
# -------------------------------------------------

"""
Exercise: Student Grade Manager (OOP)
Complete grade management system using the GradeManager class.
"""


class GradeManager:
    """
    A class to manage student grades using dictionaries.
    """

    def __init__(self):
        """Initialize empty grade database."""
        self.students = {}

    def add_student(self, student_id, name):
        """Add a new student to the database."""
        if student_id in self.students:
            print(f"[!] Student {student_id} already exists!")
            return False

        self.students[student_id] = {
            "name": name,
            "grades": {},
            "attendance": 0
        }
        print(f"[OK] Added student: {name} (ID: {student_id})")
        return True

    def add_grade(self, student_id, subject, grade):
        """Add a grade for a student in a specific subject."""
        if student_id not in self.students:
            print(f"⚠ Student {student_id} not found!")
            return False

        if not 0 <= grade <= 100:
            print(f"[!] Invalid grade: {grade}. Must be 0-100.")
            return False

        self.students[student_id]["grades"][subject] = grade
        print(f"[OK] Added {subject} grade ({grade}) for {self.students[student_id]['name']}")
        return True

    def calculate_average(self, student_id):
        """Calculate average grade for a student."""
        if student_id not in self.students:
            return None

        grades = self.students[student_id]["grades"].values()
        if not grades:
            return 0

        return sum(grades) / len(grades)

    def get_student_report(self, student_id):
        """Generate a report for a specific student."""
        if student_id not in self.students:
            print(f"⚠ Student {student_id} not found!")
            return

        student = self.students[student_id]
        print(f"\n{'=' * 50}")
        print(f"Student Report: {student['name']} (ID: {student_id})")
        print("=" * 50)

        if not student["grades"]:
            print("No grades recorded yet.")
            return

        print("\nGrades:")
        for subject, grade in sorted(student["grades"].items()):
            letter_grade = self.get_letter_grade(grade)
            print(f"  {subject:15} : {grade:5.1f} ({letter_grade})")

        average = self.calculate_average(student_id)
        print(f"\nAverage: {average:.2f} ({self.get_letter_grade(average)})")
        print("=" * 50)

    def get_letter_grade(self, numerical_grade):
        """Convert numerical grade to letter grade."""
        if numerical_grade >= 90:
            return "A"
        elif numerical_grade >= 80:
            return "B"
        elif numerical_grade >= 70:
            return "C"
        elif numerical_grade >= 60:
            return "D"
        else:
            return "F"

    def get_class_statistics(self):
        """Calculate and display statistics for the entire class."""
        if not self.students:
            print("No students in database.")
            return

        print(f"\n{'=' * 50}")
        print("Class Statistics")
        print("=" * 50)

        all_averages = []
        subject_grades = {}

        for student_id, student_data in self.students.items():
            avg = self.calculate_average(student_id)
            if avg is not None and avg > 0:
                all_averages.append(avg)

            for subject, grade in student_data["grades"].items():
                if subject not in subject_grades:
                    subject_grades[subject] = []
                subject_grades[subject].append(grade)

        if all_averages:
            class_avg = sum(all_averages) / len(all_averages)
            print(f"Class Average: {class_avg:.2f}")
            print(f"Highest Average: {max(all_averages):.2f}")
            print(f"Lowest Average: {min(all_averages):.2f}")

        print("\nSubject Averages:")
        for subject, grades in sorted(subject_grades.items()):
            avg = sum(grades) / len(grades)
            print(f"  {subject:15} : {avg:.2f}")

        print("=" * 50)

    def get_top_students(self, n=3):
        """Get the top N students by average grade."""
        student_averages = []
        for student_id, student_data in self.students.items():
            avg = self.calculate_average(student_id)
            if avg is not None and avg > 0:
                student_averages.append((student_data["name"], avg, student_id))

        student_averages.sort(key=lambda x: x[1], reverse=True)

        print(f"\nTop {n} Students:")
        print("-" * 50)
        for i, (name, avg, student_id) in enumerate(student_averages[:n], 1):
            print(f"{i}. {name:20} - Average: {avg:.2f}")


def main():
    print("Student Grade Manager (OOP)")
    print("=" * 60)

    manager = GradeManager()

    print("\n1. Adding Students:")
    print("-" * 60)
    manager.add_student("S001", "Alice Johnson")
    manager.add_student("S002", "Bob Smith")
    manager.add_student("S003", "Charlie Brown")
    manager.add_student("S004", "Diana Prince")
    print()

    print("2. Adding Grades:")
    print("-" * 60)
    manager.add_grade("S001", "Mathematics", 92)
    manager.add_grade("S001", "Science", 88)
    manager.add_grade("S001", "English", 95)
    manager.add_grade("S002", "Mathematics", 78)
    manager.add_grade("S002", "Science", 82)
    manager.add_grade("S002", "English", 85)
    manager.add_grade("S003", "Mathematics", 95)
    manager.add_grade("S003", "Science", 92)
    manager.add_grade("S003", "English", 90)
    manager.add_grade("S004", "Mathematics", 88)
    manager.add_grade("S004", "Science", 90)
    manager.add_grade("S004", "English", 87)
    print()

    print("3. Individual Student Reports:")
    print("-" * 60)
    manager.get_student_report("S001")
    manager.get_student_report("S003")

    print("\n4. Class Statistics:")
    print("-" * 60)
    manager.get_class_statistics()

    print("\n5. Top Students:")
    print("-" * 60)
    manager.get_top_students(3)

    print("\n" + "=" * 60)
    print("Summary: GradeManager class - CRUD, statistics, rankings")


if __name__ == "__main__":
    main()
