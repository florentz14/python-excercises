# -------------------------------------------------
# File: 03_attributes_methods.py
# Description: Class attributes vs instance attributes.
#              Instance methods, class methods, static methods.
# -------------------------------------------------


class Student:
    """Student class demonstrating attributes and methods."""

    # Class attribute (shared by all instances)
    school_name: str = "Python University"
    total_students: int = 0

    def __init__(self, name: str, grade: str) -> None:
        """Constructor - instance attributes."""
        self.name: str = name
        self.grade: str = grade
        self.courses: list[str] = []

        # Increment class attribute
        Student.total_students += 1

    def enroll_course(self, course_name: str) -> None:
        """Instance method - operates on instance."""
        self.courses.append(course_name)
        print(f"{self.name} enrolled in {course_name}")

    def get_info(self) -> str:
        """Instance method returning student info."""
        return f"{self.name} (Grade {self.grade}) - Courses: {self.courses}"

    @classmethod
    def get_school_info(cls) -> str:
        """Class method - operates on class, not instance."""
        return f"School: {cls.school_name}, Total students: {cls.total_students}"

    @classmethod
    def create_honors_student(cls, name: str) -> "Student":
        """Class method as alternative constructor."""
        return cls(name, "Honors")

    @staticmethod
    def is_valid_grade(grade: str) -> bool:
        """Static method - utility function, no self/cls."""
        valid_grades = ["A", "B", "C", "D", "F", "Honors"]
        return grade in valid_grades


# Demonstration
if __name__ == "__main__":
    print("=== Attributes and Methods Demo ===\n")

    # Creating instances
    student1 = Student("Alice", "A")
    student2 = Student("Bob", "B")

    print("Instance attributes:")
    print(f"student1.name: {student1.name}")
    print(f"student1.grade: {student1.grade}")
    print(f"student1.courses: {student1.courses}")

    print(f"\nClass attributes:")
    print(f"Student.school_name: {Student.school_name}")
    print(f"Student.total_students: {Student.total_students}")

    print(f"\nInstance methods:")
    student1.enroll_course("Python")
    student1.enroll_course("Data Structures")
    print(student1.get_info())

    print(f"\nClass method:")
    print(Student.get_school_info())

    print(f"\nAlternative constructor (class method):")
    honors_student = Student.create_honors_student("Charlie")
    print(honors_student.get_info())

    print(f"\nStatic method:")
    print(f"Is 'A' valid grade? {Student.is_valid_grade('A')}")
    print(f"Is 'Z' valid grade? {Student.is_valid_grade('Z')}")

    print(f"\nAll students share class attributes:")
    print(f"student1.school_name: {student1.school_name}")
    print(f"student2.school_name: {student2.school_name}")
    print(f"Student.school_name: {Student.school_name}")

    # Changing class attribute affects all instances
    Student.school_name = "Advanced Python University"
    print(f"\nAfter changing class attribute:")
    print(f"student1.school_name: {student1.school_name}")
    print(f"student2.school_name: {student2.school_name}")
