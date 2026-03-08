# -------------------------------------------------
# File Name: 42_arcade_entry_price.py
# Description: Entry price by age: <4 free, 4-18 5 EUR, >18 10 EUR
# -------------------------------------------------

age = int(input("Enter customer age: "))
if age < 4:
    price = 0
elif age <= 18:
    price = 5
else:
    price = 10
print(f"Entry price: {price} EUR")
