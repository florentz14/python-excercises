# -------------------------------------------------
# File Name: 30_weekend_check.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: Is it a weekend day?
# -------------------------------------------------

day = int(input("Enter day (1=Mon .. 7=Sun): "))

if day == 6 or day == 7:
    print("Weekend!")
else:
    print("Weekday")
