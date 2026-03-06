"""While loop: Guess the number (infinite).
Guessing game that loops until user guesses correctly.
"""
# Author: Florentino Báez


import random

# Generate a random number between 0 and 100
number = random.randint(0, 100)

print("Guess the hidden number between 0 and 100")

# Initialize guess to a value that won't match
guess = -1

# Loop until the user guesses the number
while guess != number:
    guess = int(input("Guess your number: "))

    if guess == number:
        print("Yes, you got it right!", number)
    elif guess > number:
        print("Your guess is high")
    else:
        print("Your guess is low")
