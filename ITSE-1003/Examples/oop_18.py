# -------------------------------------------------
# File Name: ITSE-1003/Examples/oop_18.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Aggregation (whole-part relationship).
# -------------------------------------------------


class Course:
    def __init__(self, name: str) -> None:
        self.name = name


class Student:
    def __init__(self, name: str) -> None:
        self.name = name
        self.courses: list[Course] = []

    def enroll(self, course: Course) -> None:
        self.courses.append(course)

    def show_courses(self) -> str:
        names = [course.name for course in self.courses]
        return f"{self.name} enrolled in: {', '.join(names)}"


def main() -> None:
    python_course = Course("Python Basics")
    sql_course = Course("SQL Fundamentals")

    student = Student("Elena")
    student.enroll(python_course)
    student.enroll(sql_course)

    print(student.show_courses())


if __name__ == "__main__":
    main()
