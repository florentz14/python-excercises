# -------------------------------------------------
# File Name: 20_leap_year_february_days.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: February Days (Leap Year)
# -------------------------------------------------

print("=" * 60)
print("EXERCISE 3: February Days (Leap Year)")
print("=" * 60)

# Get user input
# Try-except block: Handles exceptions that may occur during input conversion
try:
    year = int(input("Enter a year: "))

    # Determine if it's a leap year
    # Criteria:
    # 1. If divisible by 100, then it's a leap year if and only if also divisible by 400
    # 2. If not divisible by 100, then it's a leap year if and only if divisible by 4

    is_leap_year = False  # Initialize is_leap_year to False

    if year % 100 == 0:
        # Divisible by 100
        if year % 400 == 0:
            is_leap_year = True  # Set is_leap_year to True if year is divisible by 100 and 400
        else:
            is_leap_year = False  # Set is_leap_year to False if year is not divisible by 100 and 400
    else:
        # Not divisible by 100
        if year % 4 == 0:
            is_leap_year = True  # Set is_leap_year to True if year is not divisible by 100 and 4
        else:
            is_leap_year = False  # Set is_leap_year to False if year is not divisible by 100 and 4

    # Display the number of days in February
    if is_leap_year:
        days_in_february = 29  # Set days_in_february to 29 if year is a leap year
        print(f"In {year} February had {days_in_february} days.")
        print(f"{year} is a leap year.")
    else:
        days_in_february = 28  # Set days_in_february to 28 if year is not a leap year
        print(f"In {year} February had {days_in_february} days.")
        print(f"{year} is not a leap year.")

except ValueError:
    # Handle invalid numeric input (e.g., non-numeric characters)
    print("Error: Please enter a valid integer.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"Error: {e}")

print()
print("=" * 60)
print("Exercise completed!")
print("=" * 60)

