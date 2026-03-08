# -------------------------------------------------
# File Name: 27_parking_fee.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: Parking fee by hours
# -------------------------------------------------

hours = float(input("Hours parked: "))

if hours <= 1:
    fee = 0
elif hours <= 5:
    fee = (hours - 1) * 2
else:
    fee = 8 + (hours - 5) * 1.5  # Cap 5hrs at $8, then $1.50/hr

print(f"Parking fee: ${fee:.2f}")
