# -------------------------------------------------
# File Name: 01_number_analysis.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Professor: Mauricio Quiroga
# Date: Module 06 Lab
# Description: Number Analysis Program. Design a program that asks the user
#              to enter a series of 20 numbers. The program should store the
#              numbers in a list, and then display the following data:
#              • The lowest number on the list
#              • The highest number on the list
#              • The total of the numbers in the list
#              • The average of the numbers in the list
# -------------------------------------------------

# =============================================================================
# EXERCISE 1: Number Analysis Program
# =============================================================================

print("=" * 60)
print("EXERCISE 1: Number Analysis Program")
print("=" * 60)

# Initialize list to store numbers
numbers = []

# Get 20 numbers from user
# Try-except block: Handles exceptions that may occur during input conversion
try:
    print("Enter 20 numbers:")
    for i in range(1, 21):
        # Loop (for): Iterates 20 times to collect numbers from user
        while True:
            # Loop (while True): Continuously prompts until valid number is provided
            try:
                number = float(input(f"  Enter number {i}: "))
                numbers.append(number)  # Add number to the list
                break  # Exit the while loop when valid input is processed
            except ValueError:
                # Handle invalid numeric input (e.g., non-numeric characters)
                print("    Error: Please enter a valid number.")

    # Calculate statistics
    if numbers:
        lowest_number = min(numbers)  # Find the lowest number in the list
        highest_number = max(numbers)  # Find the highest number in the list
        total = sum(numbers)  # Calculate the sum of all numbers
        average = total / len(numbers)  # Calculate the average

        # Display results
        print("\n" + "=" * 60)
        print("NUMBER ANALYSIS RESULTS")
        print("=" * 60)
        print(f"Lowest number: {lowest_number}")
        print(f"Highest number: {highest_number}")
        print(f"Total of all numbers: {total}")
        print(f"Average of all numbers: {average:.2f}")
    else:
        print("Error: No numbers were entered.")

except Exception as e:
    # Handle any other unexpected errors
    print(f"Error: {e}")

print()

# =============================================================================
# CITATIONS
# =============================================================================
# 1. List Operations in Python:
#    - min(), max(), sum() functions for list analysis
#    - List methods: append()
#    Source: Python Documentation - Built-in Functions
#    https://docs.python.org/3/library/functions.html
#
# 2. Statistical Calculations:
#    - Average = Sum of values / Number of values
#    Source: Standard statistical methods
