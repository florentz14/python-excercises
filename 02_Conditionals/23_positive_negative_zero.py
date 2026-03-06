"""
Simple conditional: Positive, negative, or zero
================================================
Topic: Conditionals (02_Conditionals)
Description: Classify a number with if/elif/else.
"""

numero = int(input("Enter a number: "))

if numero > 0:
    print(f"{numero} is positive")
elif numero < 0:
    print(f"{numero} is negative")
else:
    print("Zero")
