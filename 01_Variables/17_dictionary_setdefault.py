# Example 16: Dictionary methods - setdefault()
print("Example 16: Dictionary methods - setdefault()")
print("-" * 40)
employee = {"id": 101, "name": "Bob", "department": "IT"}
print("Original:", employee)
print("setdefault('salary', 50000):", employee.setdefault("salary", 50000))
print("After setdefault:", employee)
print("setdefault('name', 'Unknown'):", employee.setdefault("name", "Unknown"))
print("Final dictionary:", employee)
