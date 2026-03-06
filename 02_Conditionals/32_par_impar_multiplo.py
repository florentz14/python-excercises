"""
Simple conditional: Even, odd, or multiple of 5
===============================================
Topic: Conditionals (02_Conditionals)
Description: Classify number with multiple conditions.
"""

n = int(input("Enter a number: "))

if n % 5 == 0:
    result = "Multiple of 5"
elif n % 2 == 0:
    result = "Even"
else:
    result = "Odd"

print(f"{n} → {result}")
