# -------------------------------------------------
# File Name: 40_income_tax_bands.py
# Description: Income tax rate by annual income
# -------------------------------------------------

income = float(input("Enter annual income (EUR): "))
if income < 10000:
    rate = 5
elif income < 20000:
    rate = 15
elif income < 35000:
    rate = 20
elif income < 60000:
    rate = 30
else:
    rate = 45
print(f"Tax rate: {rate}%")
