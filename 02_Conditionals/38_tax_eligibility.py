# -------------------------------------------------
# File Name: 38_tax_eligibility.py
# Description: Must be 16+ and income >= 1000 EUR to pay tax
# -------------------------------------------------

age = int(input("Enter your age: "))
income = float(input("Enter monthly income (EUR): "))
if age > 16 and income >= 1000:
    print("You must pay tax.")
else:
    print("You do not have to pay tax.")
