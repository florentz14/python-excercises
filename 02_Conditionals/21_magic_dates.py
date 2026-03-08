# -------------------------------------------------
# File Name: 21_magic_dates.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: Magic Dates
# -------------------------------------------------

print("=" * 60)
print("EXERCISE 2: Magic Dates")
print("=" * 60)

# Get user input
# Try-except block: Handles exceptions that may occur during input conversion
try:
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

except ValueError:
    # Handle invalid numeric input (e.g., non-numeric characters)
    print("Error: Please enter valid integers.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"Error: {e}")

print()
print("=" * 60)
print("Exercise completed!")
print("=" * 60)
