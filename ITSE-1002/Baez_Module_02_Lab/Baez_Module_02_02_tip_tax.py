# -------------------------------------------------
# File Name: Baez_Module_02_02_tip_tax.py
# Author: Florentino Báez
# Date: Baez_Module_02_Lab
# Description: Tip, Tax, and Total - calculates tip (18%) and sales tax (7%) for a food charge.
# -------------------------------------------------

print("=" * 60)
print("EXERCISE 2: Tip, Tax, and Total Program")
print("=" * 60)

TAX_RATE = 0.07  # 7% sales tax
TIP_RATE = 0.18  # 18% tip

food_charge = float(input("Enter the charge for the food: $"))

tip_amount = food_charge * TIP_RATE
tax_amount = food_charge * TAX_RATE
total = food_charge + tip_amount + tax_amount

print(f"\nFood charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip_amount:.2f}")
print(f"Sales tax (7%): ${tax_amount:.2f}")
print(f"Total: ${total:.2f}")

print()
