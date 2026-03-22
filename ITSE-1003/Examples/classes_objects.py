# -------------------------------------------------
# File Name: ITSE-1003/Examples/classes_objects.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Classes and Objects.
# -------------------------------------------------


class Student:
    def __init__(self, name: str, grade: int) -> None:
        self.name = name
        self.grade = grade

    def describe(self) -> str:
        return f"{self.name} is in grade {self.grade}"


def main() -> None:
    s1 = Student("Ana", 10)
    s2 = Student("Luis", 11)
    print(s1.describe())
    print(s2.describe())


if __name__ == "__main__":
    main()
