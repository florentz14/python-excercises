# -------------------------------------------------
# File: 44_lottery_number_generator.py
# Description: Lottery Number Generator.
#              Generate seven random digits (0-9).
# -------------------------------------------------

import random


def generate_lottery_number():
    """
    Generates a seven-digit lottery number.
    
    Returns:
        List of 7 random integers (0-9)
    """
    lottery_numbers = []                    # create empty list
    for _ in range(7):                      # loop 7 times
        number = random.randint(0, 9)       # random number 0-9
        lottery_numbers.append(number)      # add to list
    return lottery_numbers


def display_lottery_number(numbers):
    """
    Displays the lottery numbers.
    
    Args:
        numbers: List of lottery digits
    """
    print("Your lottery numbers are:")
    for i, num in enumerate(numbers, 1):    # loop with index
        print(f"  Digit {i}: {num}")
    
    # Also display as single string
    lottery_str = ''.join(str(n) for n in numbers)
    print(f"\nLottery Number: {lottery_str}")


def generate_lottery_formatted():
    """
    Generates and returns lottery number as formatted string.
    
    Returns:
        String with 7 digits (e.g., "3847291")
    """
    numbers = [random.randint(0, 9) for _ in range(7)]  # list comprehension
    return ''.join(str(n) for n in numbers)


# Main program
if __name__ == "__main__":
    print("=" * 40)
    print("LOTTERY NUMBER GENERATOR")
    print("=" * 40)
    
    # Generate lottery number
    lottery = generate_lottery_number()
    
    # Display the numbers
    display_lottery_number(lottery)
    
    print()
    print("-" * 40)
    print("Generate 5 more lottery numbers:")
    print("-" * 40)
    
    for i in range(5):
        number = generate_lottery_formatted()
        print(f"  Ticket {i + 1}: {number}")
