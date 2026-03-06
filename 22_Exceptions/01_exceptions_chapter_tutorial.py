# ------------------------------------------------------------
# File: 01_exceptions_chapter_tutorial.py
# Chapter: 16 - Exceptions
#
# Purpose:
#   Exceptions are errors that occur during program execution,
#   even when syntax is correct. Handling them lets the program
#   continue instead of crashing.
#
# Examples:
#   - Accessing a list index out of range
#   - Opening a file that does not exist
#   - Converting "abc" to int
#
# Sections:
#   1. try / except
#   2. Handling multiple exception types
#   3. Generic Exception and logging
#   4. else, finally, raise
#
# Author: Florentino Baez (adapted)
# ------------------------------------------------------------

import logging

# Configure logging to show exception details (optional)
logging.basicConfig(level=logging.DEBUG, format="%(message)s")


# =============================================================================
# Section 1: try / except
# Code to evaluate goes in try; error handling in except.
# =============================================================================

def divide(a: float, b: float) -> None:
    """Divide a by b. Catch ZeroDivisionError."""
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("Cannot divide by zero")


# =============================================================================
# Section 2: Handling Multiple Exception Types
# Use separate except blocks for different error types.
# =============================================================================

def pick_fruit(fruits: list[str], user_input: str) -> None:
    """
    Select fruit by index. Catches IndexError and ValueError.
    user_input: string to convert to int (simulates input()).
    """
    try:
        print(fruits)
        index = int(user_input)
        print(f"Your favorite fruit is: {fruits[index]}")
    except IndexError:
        print("That index does not exist!")
    except ValueError:
        print(f"Enter a number between 0 and {len(fruits) - 1}")


# =============================================================================
# Section 3: Generic Exception
# All exceptions inherit from Exception. Catch with 'except Exception as e'.
# =============================================================================

def pick_fruit_generic(fruits: list[str], user_input: str) -> None:
    """Same as pick_fruit but catches any Exception."""
    try:
        print(fruits)
        index = int(user_input)
        print(f"Your favorite fruit is: {fruits[index]}")
    except Exception as e:
        print(f"Error: {e}")
        logging.exception("Exception occurred: ")


# =============================================================================
# Section 4: else, finally, raise
# else: runs when no exception. finally: always runs. raise: throw an error.
# =============================================================================

def sum_numbers(input_string: str) -> float | None:
    """
    Sum numbers from a space-separated string. Raises ValueError
    if any token is non-numeric. Returns total or None on error.
    """
    try:
        total = 0.0
        tokens = input_string.split()
        for token in tokens:
            try:
                total += float(token)
            except ValueError:
                raise ValueError(f"Non-numeric value: {token!r}")
    except ValueError:
        print("Invalid data. Please enter numbers separated by spaces.")
        return None
    else:
        return total
    finally:
        print("(iteration finished)")


# =============================================================================
# Main - Run all examples
# =============================================================================

if __name__ == "__main__":
    fruits = ["0-Banana", "1-Apple", "2-Pear", "3-Peach"]

    print("=" * 55)
    print("1. try / except - Division")
    print("=" * 55)
    divide(5, 5)
    divide(5, 0)

    print("\n" + "=" * 55)
    print("2. Multiple Exception Types - pick_fruit")
    print("=" * 55)
    pick_fruit(fruits, "2")      # Valid
    pick_fruit(fruits, "10")     # IndexError
    pick_fruit(fruits, "abc")    # ValueError

    print("\n" + "=" * 55)
    print("3. Generic Exception - pick_fruit_generic")
    print("=" * 55)
    pick_fruit_generic(fruits, "xyz")

    print("\n" + "=" * 55)
    print("4. else, finally, raise - sum_numbers")
    print("=" * 55)
    result = sum_numbers("10 20 30")
    if result is not None:
        print(f"Total: {result}")
    result = sum_numbers("10 20 abc")
    if result is not None:
        print(f"Total: {result}")
