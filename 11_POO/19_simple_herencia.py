# 19_simple_herencia.py - Simple inheritance: Parent -> Child
# Florentino Baez - ITSE-1002

class Parent:
    """Base class."""
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}"

class Child(Parent):
    """Class that inherits from Parent."""
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

# Short list of children
children = [
    Child("Maria", 8),
    Child("Luis", 12),
    Child("Sofia", 5),
]

# Usage
for c in children:
    print(f"{c.greet()} (age: {c.age})")
