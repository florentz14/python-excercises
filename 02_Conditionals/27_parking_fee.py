"""
Simple conditional: Parking fee by hours
========================================
Topic: Conditionals (02_Conditionals)
Description: Calculate parking fee (first hour free, then $2/hr).
"""

hours = float(input("Hours parked: "))

if hours <= 1:
    fee = 0
elif hours <= 5:
    fee = (hours - 1) * 2
else:
    fee = 8 + (hours - 5) * 1.5  # Cap 5hrs at $8, then $1.50/hr

print(f"Parking fee: ${fee:.2f}")
