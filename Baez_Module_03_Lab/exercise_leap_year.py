# File Name: exercise_leap_year.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Professor: Mauricio Quiroga
# Date: Module 03 Lab
# Description: February Days (Leap Year)

# =============================================================================
# EXERCISE 3: February Days (Leap Year)
# =============================================================================
# Description: The month of February normally has 28 days. But if it is a leap
#              year, February has 29 days. Write a program that asks the user
#              to enter a year. The program should then display the number of
#              days in February that year. Use the following criteria to
#              identify leap years:
#              • If the year is divisible by 100, then it is a leap year if
#                and only if it is also divisible by 400.
#              • If the year is not divisible by 100, then it is a leap year
#                if and only if it is divisible by 4.
# =============================================================================

print("=" * 60)
print("EXERCISE 3: February Days (Leap Year)")
print("=" * 60)

# Get user input
year = int(input("Enter a year: "))

# Determine if it's a leap year
# Criteria:
# 1. If divisible by 100, then it's a leap year if and only if also divisible by 400
# 2. If not divisible by 100, then it's a leap year if and only if divisible by 4

if year % 100 == 0:
    # Divisible by 100
    if year % 400 == 0:
        is_leap_year = True
    else:
        is_leap_year = False
else:
    # Not divisible by 100
    if year % 4 == 0:
        is_leap_year = True
    else:
        is_leap_year = False

# Display the number of days in February
if is_leap_year:
    days_in_february = 29
    print(f"In {year} February had {days_in_february} days.")
    print(f"{year} is a leap year.")
else:
    days_in_february = 28
    print(f"In {year} February had {days_in_february} days.")
    print(f"{year} is not a leap year.")
