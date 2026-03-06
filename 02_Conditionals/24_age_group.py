"""
Simple conditional: Age group classifier
========================================
Topic: Conditionals (02_Conditionals)
Description: Classify person as child, teen, adult, or senior.
"""

age = int(input("Enter your age: "))

if age < 13:
    group = "child"
elif age < 20:
    group = "teen"
elif age < 65:
    group = "adult"
else:
    group = "senior"

print(f"Age {age} → {group}")
