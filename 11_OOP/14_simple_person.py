# 14_simple_persona.py - Simple class: Person (attributes only)
# Florentino Baez - ITSE-1002

class Person:
    """Simple class with only __init__ and attributes."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Short list of persons
persons = [
    Person("Ana", 25),
    Person("Bob", 30),
    Person("Carol", 22),
]

# Usage
for p in persons:
    print(f"{p.name}, {p.age} years old")
