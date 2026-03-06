# -------------------------------------------------
# File Name: 22_grade_manager.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Student Grade Manager.
#              Creates a complete grade management system using
#              nested dictionaries. Implements CRUD operations,
#              grade letter conversion, individual reports, class
#              statistics, and top-student rankings.
# -------------------------------------------------

"""
Exercise 6: Student Grade Manager
This exercise creates a complete grade management system using dictionaries.
Demonstrates practical use of nested dictionaries and various operations.
"""

class GradeManager:
    """
    A class to manage student grades using dictionaries.
    """
    
    def __init__(self):
        """Initialize empty grade database."""
        # Main dictionary: student_id -> student data (nested dict)
        self.students = {}
    
    def add_student(self, student_id, name):
        """
        Add a new student to the database.
        
        Args:
            student_id: Unique identifier for student
            name: Student's name
        """
        # Check if student already exists in database
        if student_id in self.students:
            print(f"⚠ Student {student_id} already exists!")
            return False
        
        # Create nested dictionary structure for new student
        self.students[student_id] = {
            "name": name,
            "grades": {},  # Dictionary: subject -> grade
            "attendance": 0
        }
        print(f"✓ Added student: {name} (ID: {student_id})")
        return True
    
    def add_grade(self, student_id, subject, grade):
        """
        Add a grade for a student in a specific subject.
        
        Args:
            student_id: Student's ID
            subject: Subject name
            grade: Grade value (0-100)
        """
        # Validate student exists
        if student_id not in self.students:
            print(f"⚠ Student {student_id} not found!")
            return False
        
        # Validate grade is within valid range (0-100)
        if not 0 <= grade <= 100:
            print(f"⚠ Invalid grade: {grade}. Must be 0-100.")
            return False
        
        # Add grade to nested dictionary: student -> grades -> subject
        self.students[student_id]["grades"][subject] = grade
        print(f"✓ Added {subject} grade ({grade}) for {self.students[student_id]['name']}")
        return True
    
    def calculate_average(self, student_id):
        """
        Calculate average grade for a student.
        
        Args:
            student_id: Student's ID
        
        Returns:
            Average grade or None if student not found
        """
        # Check if student exists
        if student_id not in self.students:
            return None
        
        # Get all grade values from the nested grades dictionary
        grades = self.students[student_id]["grades"].values()
        if not grades:  # No grades recorded yet
            return 0
        
        # Calculate arithmetic mean of all grades
        return sum(grades) / len(grades)
    
    def get_student_report(self, student_id):
        """
        Generate a report for a specific student.
        
        Args:
            student_id: Student's ID
        """
        # Validate student exists
        if student_id not in self.students:
            print(f"⚠ Student {student_id} not found!")
            return
        
        # Get student data from nested dictionary
        student = self.students[student_id]
        print(f"\n{'=' * 50}")
        print(f"Student Report: {student['name']} (ID: {student_id})")
        print("=" * 50)
        
        # Check if student has any grades
        if not student["grades"]:
            print("No grades recorded yet.")
            return
        
        # Display all grades sorted alphabetically by subject
        print("\nGrades:")
        for subject, grade in sorted(student["grades"].items()):
            letter_grade = self.get_letter_grade(grade)  # Convert to letter grade
            print(f"  {subject:15} : {grade:5.1f} ({letter_grade})")
        
        # Calculate and display overall average
        average = self.calculate_average(student_id)
        print(f"\nAverage: {average:.2f} ({self.get_letter_grade(average)})")
        print("=" * 50)
    
    def get_letter_grade(self, numerical_grade):
        """
        Convert numerical grade to letter grade.
        
        Args:
            numerical_grade: Grade (0-100)
        
        Returns:
            Letter grade (A, B, C, D, F)
        """
        # Convert numerical grade to letter grade using standard scale
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
        """
        Calculate and display statistics for the entire class.
        """
        if not self.students:
            print("No students in database.")
            return
        
        print(f"\n{'=' * 50}")
        print("Class Statistics")
        print("=" * 50)
        
        # Initialize data structures for statistics
        all_averages = []  # Store average grade for each student
        subject_grades = {}  # Dictionary: subject -> list of all grades
        
        # Iterate through all students to collect data
        for student_id, student_data in self.students.items():
            avg = self.calculate_average(student_id)
            if avg > 0:  # Only include students with recorded grades
                all_averages.append(avg)
            
            # Collect grades by subject for subject-level statistics
            for subject, grade in student_data["grades"].items():
                if subject not in subject_grades:
                    subject_grades[subject] = []
                subject_grades[subject].append(grade)
        
        # Calculate and display class-level statistics
        if all_averages:
            class_avg = sum(all_averages) / len(all_averages)
            print(f"Class Average: {class_avg:.2f}")
            print(f"Highest Average: {max(all_averages):.2f}")
            print(f"Lowest Average: {min(all_averages):.2f}")
        
        # Calculate and display average grade per subject
        print("\nSubject Averages:")
        for subject, grades in sorted(subject_grades.items()):
            avg = sum(grades) / len(grades)  # Mean grade for this subject
            print(f"  {subject:15} : {avg:.2f}")
        
        print("=" * 50)
    
    def get_top_students(self, n=3):
        """
        Get the top N students by average grade.
        
        Args:
            n: Number of top students to return
        """
        # Calculate averages for all students and store as tuples
        student_averages = []
        for student_id, student_data in self.students.items():
            avg = self.calculate_average(student_id)
            if avg > 0:  # Only include students with recorded grades
                # Tuple: (name, average, student_id) for sorting
                student_averages.append((student_data["name"], avg, student_id))
        
        # Sort by average grade (descending): key=lambda x: x[1] uses the average
        student_averages.sort(key=lambda x: x[1], reverse=True)
        
        # Display top N students
        print(f"\nTop {n} Students:")
        print("-" * 50)
        for i, (name, avg, student_id) in enumerate(student_averages[:n], 1):
            print(f"{i}. {name:20} - Average: {avg:.2f}")


def main():
    print("Exercise 6: Student Grade Manager")
    print("=" * 60)
    
    # Create grade manager instance
    manager = GradeManager()
    
    print("\n1. Adding Students:")
    print("-" * 60)
    # Add students to the database
    manager.add_student("S001", "Alice Johnson")
    manager.add_student("S002", "Bob Smith")
    manager.add_student("S003", "Charlie Brown")
    manager.add_student("S004", "Diana Prince")
    print()
    
    print("2. Adding Grades:")
    print("-" * 60)
    # Add grades for Alice
    manager.add_grade("S001", "Mathematics", 92)
    manager.add_grade("S001", "Science", 88)
    manager.add_grade("S001", "English", 95)
    
    # Add grades for Bob
    manager.add_grade("S002", "Mathematics", 78)
    manager.add_grade("S002", "Science", 82)
    manager.add_grade("S002", "English", 85)
    
    # Add grades for Charlie
    manager.add_grade("S003", "Mathematics", 95)
    manager.add_grade("S003", "Science", 92)
    manager.add_grade("S003", "English", 90)
    
    # Add grades for Diana
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
    print("Summary:")
    print("  - Used nested dictionaries for complex data")
    print("  - Implemented CRUD operations (Create, Read, Update, Delete)")
    print("  - Calculated statistics and rankings")
    print("  - Demonstrated practical dictionary applications")


if __name__ == "__main__":
    main()
