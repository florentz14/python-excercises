# -------------------------------------------------
# File: 16_classmethod.py
# Description: @classmethod decorator.
#              Methods that operate on the class, not instances.
# -------------------------------------------------

from typing import TypeVar

T = TypeVar("T", bound="Student")


class Student:
    """Student class with class methods."""

    school_name = "Python University"
    total_students = 0

    def __init__(self, name: str, student_id: str) -> None:
        self.name: str = name
        self.student_id: str = student_id
        Student.total_students += 1

    @classmethod
    def get_school_info(cls: type[T]) -> str:
        """Class method to get school information."""
        return f"School: {cls.school_name}, Total students: {cls.total_students}"

    @classmethod
    def change_school_name(cls: type[T], new_name: str) -> None:
        """Class method to change school name for all students."""
        cls.school_name = new_name
        print(f"School name changed to: {new_name}")

    @classmethod
    def create_student(cls, name, student_id):
        """Class method as alternative constructor."""
        print(f"Creating student via class method: {name}")
        return cls(name, student_id)

    def get_info(self):
        """Instance method."""
        return f"Student: {self.name}, ID: {self.student_id}, School: {self.school_name}"


class Date:
    """Date class with class methods for different input formats."""

    def __init__(self, year: int, month: int, day: int) -> None:
        self.year: int = year
        self.month: int = month
        self.day: int = day

    @classmethod
    def from_string(cls: type["Date"], date_string: str) -> "Date":
        """Create Date from string 'YYYY-MM-DD'."""
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)

    @classmethod
    def from_timestamp(cls, timestamp):
        """Create Date from Unix timestamp."""
        import datetime
        dt = datetime.datetime.fromtimestamp(timestamp)
        return cls(dt.year, dt.month, dt.day)

    @classmethod
    def today(cls: type["Date"]) -> "Date":
        """Create Date for today."""
        import datetime
        today = datetime.date.today()
        return cls(today.year, today.month, today.day)

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"


class ShapeFactory:
    """Factory class using class methods."""

    @classmethod
    def create_circle(cls: type["ShapeFactory"], radius: float) -> str:
        """Create a circle."""
        return f"Circle with radius {radius}"

    @classmethod
    def create_rectangle(cls, width, height):
        """Create a rectangle."""
        return f"Rectangle {width}x{height}"

    @classmethod
    def create_square(cls, side):
        """Create a square."""
        return f"Square with side {side}"


# Demonstration
if __name__ == "__main__":
    print("=== @classmethod Demo ===\n")

    # Student class methods
    print("Student class methods:")
    print(Student.get_school_info())

    student1 = Student("Alice", "S001")
    student2 = Student("Bob", "S002")

    print(Student.get_school_info())

    # Change school name (affects all)
    Student.change_school_name("Advanced Python Academy")
    print(Student.get_school_info())
    print(f"Individual student: {student1.get_info()}")

    # Alternative constructor
    student3 = Student.create_student("Charlie", "S003")
    print(f"New student: {student3.get_info()}")
    print(f"Total students: {Student.total_students}")

    print("\n=== Date Class Methods ===")

    # Different ways to create Date objects
    date1 = Date(2023, 12, 25)
    date2 = Date.from_string("2024-01-01")
    date3 = Date.today()

    print(f"Regular constructor: {date1}")
    print(f"From string: {date2}")
    print(f"Today: {date3}")

    # From timestamp
    import time
    timestamp = time.time()
    date4 = Date.from_timestamp(timestamp)
    print(f"From timestamp: {date4}")

    print("\n=== Factory Pattern with Class Methods ===")

    shapes = [
        ShapeFactory.create_circle(5),
        ShapeFactory.create_rectangle(4, 6),
        ShapeFactory.create_square(3)
    ]

    for shape in shapes:
        print(f"Created: {shape}")

    print("\n=== Class Method Characteristics ===")
    print("- First parameter is 'cls' (convention)")
    print("- Can access class attributes and methods")
    print("- Can be called on class or instance")
    print("- Cannot access instance attributes (no 'self')")
    print("- Often used for alternative constructors")
    print("- Useful for factory patterns")

    print("\n=== When to Use Class Methods ===")
    print("- Alternative constructors (from_string, from_dict, etc.)")
    print("- Factory methods")
    print("- Operations that affect the entire class")
    print("- When you need to access class-level data")