# -------------------------------------------------
# File Name: ITSE-1003/Examples/class_instance_attrs.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Class vs instance attributes.
# -------------------------------------------------


class Student:
    school_name = "Central High"

    def __init__(self, name: str) -> None:
        self.name = name


def main() -> None:
    s1 = Student("Mia")
    s2 = Student("Noah")

    print("Shared class attribute:", Student.school_name)
    print("s1 school:", s1.school_name)
    print("s2 school:", s2.school_name)

    s1.school_name = "Private Academy"
    print("\nAfter overriding on s1 instance:")
    print("Student.school_name:", Student.school_name)
    print("s1 school:", s1.school_name)
    print("s2 school:", s2.school_name)


if __name__ == "__main__":
    main()
