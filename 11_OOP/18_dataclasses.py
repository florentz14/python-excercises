# -------------------------------------------------
# File Name: 18_dataclasses.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: @dataclass decorator.
# -------------------------------------------------

from dataclasses import dataclass, field
from typing import List, Optional
import datetime


@dataclass
class Person:
    """Basic dataclass example."""
    name: str
    age: int
    email: str = ""  # Default value

    def greet(self):
        """Regular method still works."""
        return f"Hello, I'm {self.name}, {self.age} years old."


@dataclass
class Point:
    """2D point with automatic __init__, __repr__, __eq__."""
    x: float
    y: float

    def distance_from_origin(self):
        """Calculate distance from origin."""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance_to(self, other: 'Point'):
        """Calculate distance to another point."""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


@dataclass
class Rectangle:
    """Rectangle with computed properties."""
    width: float
    height: float

    @property
    def area(self):
        """Calculate area."""
        return self.width * self.height

    @property
    def perimeter(self):
        """Calculate perimeter."""
        return 2 * (self.width + self.height)


@dataclass
class Student:
    """Student with mutable default values."""
    name: str
    grades: List[int] = field(default_factory=list)  # Mutable default

    def add_grade(self, grade: int):
        """Add a grade."""
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100")

    @property
    def average_grade(self):
        """Calculate average grade."""
        return sum(self.grades) / len(self.grades) if self.grades else 0


@dataclass(frozen=True)
class ImmutablePoint:
    """Immutable dataclass - cannot be modified after creation."""
    x: float
    y: float


@dataclass(order=True)
class OrderedPerson:
    """Dataclass with ordering support."""
    sort_index: int = field(init=False, repr=False)
    name: str
    age: int

    def __post_init__(self):
        """Set sort index after initialization."""
        self.sort_index = self.age


@dataclass
class Employee:
    """Employee with validation."""
    name: str
    salary: float
    department: str = "General"

    def __post_init__(self):
        """Validate data after initialization."""
        if self.salary < 0:
            raise ValueError("Salary cannot be negative")
        if not self.name:
            raise ValueError("Name cannot be empty")


@dataclass
class Book:
    """Book with optional fields."""
    title: str
    author: str
    isbn: Optional[str] = None
    published_year: Optional[int] = None
    genres: List[str] = field(default_factory=list)

    def add_genre(self, genre: str):
        """Add a genre."""
        if genre not in self.genres:
            self.genres.append(genre)

    def __str__(self):
        """Custom string representation."""
        year_str = f" ({self.published_year})" if self.published_year else ""
        return f"'{self.title}' by {self.author}{year_str}"


@dataclass
class Address:
    """Address dataclass."""
    street: str
    city: str
    state: str
    zip_code: str


@dataclass
class Contact:
    """Contact with nested dataclass."""
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[Address] = None


@dataclass
class Task:
    """Task with automatic timestamp."""
    description: str
    completed: bool = False
    created_at: datetime.datetime = field(
        default_factory=datetime.datetime.now)
    completed_at: Optional[datetime.datetime] = None

    def mark_complete(self):
        """Mark task as complete."""
        self.completed = True
        self.completed_at = datetime.datetime.now()


# Demonstration
if __name__ == "__main__":
    print("=== @dataclass Demo ===\n")

    # Basic dataclass
    print("Basic dataclass:")
    person = Person("Alice", 30, "alice@example.com")
    print(f"Person: {person}")
    print(f"Greet: {person.greet()}")

    # Point operations
    print("\nPoint operations:")
    p1 = Point(3, 4)
    p2 = Point(0, 0)
    print(f"Point 1: {p1}")
    print(f"Distance from origin: {p1.distance_from_origin()}")
    print(f"Distance between points: {p1.distance_to(p2)}")

    # Rectangle properties
    print("\nRectangle properties:")
    rect = Rectangle(5, 3)
    print(f"Rectangle: {rect}")
    print(f"Area: {rect.area}")
    print(f"Perimeter: {rect.perimeter}")

    # Student with grades
    print("\nStudent grades:")
    student = Student("Bob")
    student.add_grade(85)
    student.add_grade(92)
    student.add_grade(78)
    print(f"Student: {student}")
    print(f"Average grade: {student.average_grade:.1f}")

    # Immutable dataclass
    print("\nImmutable dataclass:")
    immutable_point = ImmutablePoint(1, 2)
    print(f"Immutable point: {immutable_point}")
    # immutable_point.x = 5  # This would raise FrozenInstanceError

    # Ordered dataclass
    print("\nOrdered dataclass:")
    people = [
        OrderedPerson("Charlie", 25),
        OrderedPerson("Alice", 30),
        OrderedPerson("Bob", 20)
    ]
    print("Before sorting:", [p.name for p in people])
    people.sort()
    print("After sorting by age:", [p.name for p in people])

    # Employee validation
    print("\nEmployee validation:")
    try:
        emp = Employee("David", 50000, "Engineering")
        print(f"Employee: {emp}")
    except ValueError as e:
        print(f"Error: {e}")

    # Book with custom __str__
    print("\nBook representation:")
    book = Book("1984", "George Orwell", "978-0451524935",
                1949, ["Dystopian", "Fiction"])
    print(f"Book: {book}")

    # Nested dataclasses
    print("\nNested dataclasses:")
    addr = Address("123 Main St", "Anytown", "CA", "12345")
    contact = Contact("Eve", "eve@example.com", "555-0123", addr)
    print(f"Contact: {contact}")

    # Task with timestamps
    print("\nTask with timestamps:")
    task = Task("Learn Python dataclasses")
    print(f"Created task: {task}")
    import time
    time.sleep(1)  # Wait 1 second
    task.mark_complete()
    print(f"Completed task: {task}")

    print("\n=== Dataclass Features ===")
    print("- Automatic __init__, __repr__, __eq__ generation")
    print("- Type hints become constructor parameters")
    print("- field() for advanced customization")
    print("- frozen=True for immutability")
    print("- order=True for comparison operators")
    print("- __post_init__ for validation/customization")

    print("\n=== When to Use Dataclasses ===")
    print("- Data storage classes")
    print("- Simple data structures")
    print("- When you want automatic methods")
    print("- Configuration objects")
    print("- DTOs (Data Transfer Objects)")
    print("- When immutability is desired")

    print("\n=== Comparison with Regular Classes ===")
    print("Dataclass: Automatic boilerplate, less code")
    print("Regular class: Full control, more flexibility")
    print("Both can have methods and properties")
