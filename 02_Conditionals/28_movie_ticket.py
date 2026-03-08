# -------------------------------------------------
# File Name: 28_movie_ticket.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: Movie ticket price by age
# -------------------------------------------------

age = int(input("Enter age: "))

if age < 12:
    price = 5
elif age >= 65:
    price = 6
else:
    price = 10

print(f"Ticket price: ${price}")
