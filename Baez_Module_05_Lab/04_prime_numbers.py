#!/usr/bin/env python3
"""Baez Module 05 Lab - Exercise 4
Prime Numbers
"""

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    print("=" * 60)
    print("EXERCISE 4: Prime Numbers")
    print("=" * 60)
    try:
        number = int(input("Enter a number to check if it is prime: "))
        if is_prime(number):
            print(f"\n{number} is a prime number.")
        else:
            print(f"\n{number} is not a prime number.")
    except ValueError:
        print("Error: Please enter a valid integer.")
    except Exception as e:
        print(f"Error: {e}")
