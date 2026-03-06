"""
Simple conditional: Is it a weekend day?
=======================================
Topic: Conditionals (02_Conditionals)
Description: Check if day number (1-7) is weekend.
"""

day = int(input("Enter day (1=Mon .. 7=Sun): "))

if day == 6 or day == 7:
    print("Weekend!")
else:
    print("Weekday")
