"""
Simple conditional: Discount by purchase amount
================================================
Topic: Conditionals (02_Conditionals)
Description: Apply discount based on total purchase.
"""

total = float(input("Enter purchase total: $"))

if total >= 200:
    discount = 0.15  # 15%
elif total >= 100:
    discount = 0.10  # 10%
elif total >= 50:
    discount = 0.05  # 5%
else:
    discount = 0

final = total * (1 - discount)
print(f"Total: ${total:.2f} | Discount: {discount*100:.0f}% | You pay: ${final:.2f}")
