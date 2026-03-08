# -------------------------------------------------
# File Name: 22_roman_numeral_converter.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: Roman Numeral Converter
# -------------------------------------------------

print("=" * 60)
print("EXERCISE 1: Roman Numeral Converter")
print("=" * 60)

# Get user input with validation
# Loop (while True): Continuously prompts the user until valid input is provided
while True:
    # Try-except block: Handles exceptions that may occur during input conversion
    try:
        number = int(
            input("Enter a number within the range of 1 through 10: "))

        # Input validation: Do not accept a number less than 1 or greater than 10
        if number < 1 or number > 10:
            print("Error: Please enter a number between 1 and 10.")
            continue  # Continue loop to ask for input again

        # Convert to Roman numeral using if-elif statements
        if number == 1:
            roman_numeral = "I"
        elif number == 2:
            roman_numeral = "II"
        elif number == 3:
            roman_numeral = "III"
        elif number == 4:
            roman_numeral = "IV"
        elif number == 5:
            roman_numeral = "V"
        elif number == 6:
            roman_numeral = "VI"
        elif number == 7:
            roman_numeral = "VII"
        elif number == 8:
            roman_numeral = "VIII"
        elif number == 9:
            roman_numeral = "IX"
        else:  # number == 10
            roman_numeral = "X"

        print(f"The Roman numeral version of {number} is: {roman_numeral}")
        break  # Exit the loop when valid input is processed

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
