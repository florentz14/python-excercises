#!/usr/bin/env python3
# -------------------------------------------------
# File Name: 04_prime_numbers.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Professor: Mauricio Quiroga
# Date: Module 05 Lab
# Description: Determine whether a number is prime.
# -------------------------------------------------

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


print("=" * 60)
print("EXERCISE 4: Prime Numbers")
print("=" * 60)

number = int(input("Enter a number to check if it is prime: "))
if is_prime(number):
    print(f"\n{number} is a prime number.")
else:
    print(f"\n{number} is not a prime number.")

print()

print("\n" + "=" * 60)
print("CITATION")
print("=" * 60)
print("1. Prime Number Algorithm:")
print("   - Trial division method: Check divisibility from 2 to √n")
print("   Source: Prime Number - Wikipedia")
print("   https://en.wikipedia.org/wiki/Prime_number")
