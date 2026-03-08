# -------------------------------------------------
# File Name: exercise_magic_dates.py
# Author: Florentino Báez
# Date: Baez_Module_03_Lab
# Description: Magic Dates
# -------------------------------------------------

print("=" * 60)
print("EXERCISE 2: Magic Dates")
print("=" * 60)

# Get user input
month = int(input("Enter a month (in numeric form, 1-12): "))
day = int(input("Enter a day: "))
year = int(input("Enter a two-digit year: "))

# Check if the date is magic
# A date is magic if month * day equals the year
if month * day == year:
    print(f"\nThe date {month}/{day}/{year:02d} is a MAGIC DATE!")
    print(
        f"Because {month} x {day} = {month * day}, which equals the year {year:02d}")
else:
    print(f"\nThe date {month}/{day}/{year:02d} is NOT a magic date.")
    print(
        f"Because {month} x {day} = {month * day}, which does not equal the year {year:02d}")
