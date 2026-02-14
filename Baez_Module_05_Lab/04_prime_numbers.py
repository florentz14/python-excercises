# -------------------------------------------------
# File Name: 04_prime_numbers.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Professor: Mauricio Quiroga
# Date: Module 05 Lab
# Description: Determine whether a number is prime.
# -------------------------------------------------

# Check if a number is prime
def is_prime(number: int) -> bool:
    # Numbers less than 2 are not prime
    if number < 2:
        return False
    # Loop: Iterate through the range of numbers from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        # If the number is divisible by i, it is not prime
        if number % i == 0:
            return False
    # If the number is not divisible by any number in the range, it is prime
    return True


print("=" * 60)
print("EXERCISE 4: Prime Numbers")
print("=" * 60)

# Get user input
number = int(input("Enter a number to check if it is prime: "))

# Check if the number is prime
if is_prime(number):
    # Display results
    print(f"\n{number} is a prime number.")
else:
    print(f"\n{number} is not a prime number.")

print()
