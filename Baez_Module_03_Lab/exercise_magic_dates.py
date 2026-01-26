# File Name: exercise_magic_dates.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Professor: Mauricio Quiroga
# Date: Module 03 Lab
# Description: Magic Dates

# =============================================================================
# EXERCISE 2: Magic Dates
# =============================================================================
# Description: The date June 10, 1960, is special because when we write it in
#              the following format, the month times the day equals the year:
#              6/10/60. Write a program that asks the user to enter a month
#              (in numeric form), a day, and a two-digit year. The program
#              should then determine whether the month times the day equals the
#              year. If so, it should display a message saying the date is
#              magic. Otherwise, it should display a message saying the date is
#              not magic.
# =============================================================================

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
