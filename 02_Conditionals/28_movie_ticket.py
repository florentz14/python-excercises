"""
Simple conditional: Movie ticket price by age
=============================================
Topic: Conditionals (02_Conditionals)
Description: Different prices for child, adult, senior.
"""

age = int(input("Enter age: "))

if age < 12:
    price = 5
elif age >= 65:
    price = 6
else:
    price = 10

print(f"Ticket price: ${price}")
