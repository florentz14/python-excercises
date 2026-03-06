# -------------------------------------------------
# File: 45_lottery_number_generator_v2.py
# Description: Lottery Number Generator (Version 2).
#              Using constants and pre-initialized list.
# -------------------------------------------------

import random

MAX_DIGITS = 7  # Max number of digits
START = 0       # Start of the random number range
END = 9         # End of the random number range


def main():
    """Main function using constants and index-based assignment."""
    # Create a list with 7 zeros
    numbers = [0] * MAX_DIGITS
    
    # Populate the list with random numbers
    for index in range(MAX_DIGITS):
        numbers[index] = random.randint(START, END)
    
    # Display the random numbers
    print('Here are your lottery numbers:')
    for index in range(MAX_DIGITS):
        print(numbers[index], end='')
    print()


# Call the main function
if __name__ == "__main__":
    main()
