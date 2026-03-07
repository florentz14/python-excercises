# -------------------------------------------------
# File: 21_person.py
# Description: Person class - practical application.
#              Encapsulation, validation, methods.
# -------------------------------------------------

from datetime import datetime, date
from typing import Optional, List


class Person:
    """Person class demonstrating OOP concepts."""

    def __init__(self, first_name: str, last_name: str, birth_date: date):
        self._first_name = ""
        self._last_name = ""
        self._birth_date: date = birth_date  # Will be set via setter
        self._email: Optional[str] = None
        self._phone: Optional[str] = None

        # Use setters for validation
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    @property
    def first_name(self) -> str:
        """Get first name."""
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        """Set first name with validation."""
        if not value or not value.strip():
            raise ValueError("First name cannot be empty")
        if not all(c.isalpha() or c.isspace() for c in value):
            raise ValueError("First name can only contain letters and spaces")
        self._first_name = value.strip().title()

    @property
    def last_name(self) -> str:
        """Get last name."""
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        """Set last name with validation."""
        if not value or not value.strip():
            raise ValueError("Last name cannot be empty")
        if not all(c.isalpha() or c.isspace() for c in value):
            raise ValueError("Last name can only contain letters and spaces")
        self._last_name = value.strip().title()

    @property
    def full_name(self) -> str:
        """Get full name."""
        return f"{self._first_name} {self._last_name}"

    @property
    def birth_date(self) -> date:
        """Get birth date."""
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value: date):
        """Set birth date with validation."""
        if value > date.today():
            raise ValueError("Birth date cannot be in the future")
        # Reasonable age limit
        if (date.today() - value).days > 365 * 150:
            raise ValueError("Age cannot exceed 150 years")
        self._birth_date = value

    @property
    def age(self) -> int:
        """Calculate current age."""
        today = date.today()
        age = today.year - self._birth_date.year
        # Adjust if birthday hasn't occurred this year
        if (today.month, today.day) < (self._birth_date.month, self._birth_date.day):
            age -= 1
        return age

    @property
    def email(self) -> Optional[str]:
        """Get email."""
        return self._email

    @email.setter
    def email(self, value: Optional[str]):
        """Set email with validation."""
        if value is not None:
            if '@' not in value or '.' not in value.split('@')[1]:
                raise ValueError("Invalid email format")
        self._email = value

    @property
    def phone(self) -> Optional[str]:
        """Get phone number."""
        return self._phone

    @phone.setter
    def phone(self, value: Optional[str]):
        """Set phone number with validation."""
        if value is not None:
            # Remove all non-digit characters
            digits = ''.join(c for c in value if c.isdigit())
            if len(digits) < 10:
                raise ValueError("Phone number must have at least 10 digits")
            # Format as (XXX) XXX-XXXX
            self._phone = f"({digits[:3]}) {digits[3:6]}-{digits[6:10]}"
        else:
            self._phone = None

    def get_info(self) -> str:
        """Get person information."""
        info = f"Name: {self.full_name}\n"
        info += f"Age: {self.age} years old\n"
        # type: ignore
        info += f"Birth Date: {self._birth_date.strftime('%B %d, %Y')}\n"
        if self._email:
            info += f"Email: {self._email}\n"
        if self._phone:
            info += f"Phone: {self._phone}\n"
        return info.strip()

    def can_vote(self) -> bool:
        """Check if person can vote (18+ years old)."""
        return self.age >= 18

    def is_senior(self) -> bool:
        """Check if person is a senior (65+ years old)."""
        return self.age >= 65

    def get_age_group(self) -> str:
        """Get age group category."""
        if self.age < 13:
            return "Child"
        elif self.age < 20:
            return "Teenager"
        elif self.age < 65:
            return "Adult"
        else:
            return "Senior"

    def celebrate_birthday(self) -> str:
        """Celebrate birthday."""
        new_age = self.age + 1
        return f"Happy Birthday {self._first_name}! You are now {new_age} years old!"

    def __str__(self) -> str:
        """String representation."""
        return self.full_name

    def __repr__(self) -> str:
        """Detailed string representation."""
        return f"Person('{self._first_name}', '{self._last_name}', {self._birth_date!r})"

    def __eq__(self, other) -> bool:
        """Check equality based on full name and birth date."""
        if not isinstance(other, Person):
            return False
        return (self.full_name == other.full_name and
                self._birth_date == other._birth_date)

    def __lt__(self, other) -> bool:
        """Compare by last name, then first name."""
        if not isinstance(other, Person):
            return NotImplemented
        return (self._last_name, self._first_name) < (other._last_name, other._first_name)


class Student(Person):
    """Student subclass of Person."""

    def __init__(self, first_name: str, last_name: str, birth_date: date,
                 student_id: str, major: str = "Undeclared"):
        super().__init__(first_name, last_name, birth_date)
        self.student_id = student_id
        self.major = major
        self._grades = []  # List of grade dictionaries
        self._enrolled_courses = []

    def enroll_course(self, course_name: str, course_code: str):
        """Enroll in a course."""
        course = {"name": course_name, "code": course_code, "grade": None}
        if course not in self._enrolled_courses:
            self._enrolled_courses.append(course)
            return f"Enrolled in {course_name} ({course_code})"
        return f"Already enrolled in {course_name}"

    def add_grade(self, course_code: str, grade: float):
        """Add grade for a course."""
        for course in self._enrolled_courses:
            if course["code"] == course_code:
                course["grade"] = grade
                return f"Grade {grade} added for {course['name']}"
        return f"Course {course_code} not found"

    def get_gpa(self) -> float:
        """Calculate GPA."""
        grades = [course["grade"] for course in self._enrolled_courses
                  if course["grade"] is not None]
        return sum(grades) / len(grades) if grades else 0.0

    def get_enrolled_courses(self) -> List[str]:
        """Get list of enrolled courses."""
        return [f"{course['name']} ({course['code']})" for course in self._enrolled_courses]

    def get_info(self) -> str:
        """Get student information."""
        info = super().get_info()
        info += f"\nStudent ID: {self.student_id}"
        info += f"\nMajor: {self.major}"
        info += f"\nGPA: {self.get_gpa():.2f}"
        if self._enrolled_courses:
            info += f"\nEnrolled Courses: {', '.join(self.get_enrolled_courses())}"
        return info


# Demonstration
if __name__ == "__main__":
    print("=== Person Class Demo ===\n")

    # Create a person
    birth_date = date(1995, 6, 15)
    person = Person("john", "doe", birth_date)

    # Set contact info
    person.email = "john.doe@example.com"
    person.phone = "555-123-4567"

    print("Person Information:")
    print(person.get_info())

    print(f"\nCan vote: {person.can_vote()}")
    print(f"Is senior: {person.is_senior()}")
    print(f"Age group: {person.get_age_group()}")

    print(f"\nBirthday celebration: {person.celebrate_birthday()}")

    # Create another person for comparison
    person2 = Person("Jane", "Smith", date(1990, 3, 20))
    person2.email = "jane.smith@example.com"

    print(f"\nComparison:")
    print(f"{person.full_name} == {person2.full_name}: {person == person2}")
    print(f"{person.full_name} < {person2.full_name}: {person < person2}")

    # Student example
    print("\n=== Student Class Demo ===\n")

    student = Student("Alice", "Johnson", date(
        2000, 9, 1), "S12345", "Computer Science")

    # Enroll in courses
    student.enroll_course("Introduction to Programming", "CS101")
    student.enroll_course("Data Structures", "CS201")
    student.enroll_course("Algorithms", "CS301")

    # Add grades
    student.add_grade("CS101", 3.7)
    student.add_grade("CS201", 4.0)
    student.add_grade("CS301", 3.3)

    print("Student Information:")
    print(student.get_info())

    print(f"\nEnrolled courses: {student.get_enrolled_courses()}")
    print(f"Current GPA: {student.get_gpa():.2f}")

    print("\n=== OOP Concepts Demonstrated ===")
    print("- Encapsulation: Private attributes with property accessors")
    print("- Validation: Input validation in setters")
    print("- Inheritance: Student inherits from Person")
    print("- Polymorphism: Student overrides get_info()")
    print("- Magic methods: __str__, __repr__, __eq__, __lt__")
    print("- Properties: Computed attributes (age, full_name)")
    print("- Methods: Business logic and utility functions")

    print("\n=== Error Handling Demo ===")
    try:
        invalid_person = Person("", "Smith", date.today())
    except ValueError as e:
        print(f"Validation error: {e}")

    try:
        person.email = "invalid-email"
    except ValueError as e:
        print(f"Email validation error: {e}")

    try:
        person.phone = "123"
    except ValueError as e:
        print(f"Phone validation error: {e}")
