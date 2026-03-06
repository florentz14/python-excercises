"""
While loop: Guess the number game.
User guesses secret number (1-10) with feedback until correct.

# Author: Florentino Báez
"""

print("Example: Guess the number (1-10)")
print("-" * 40)

secret_number = 7
guess = 0
attempts = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1
    if guess < secret_number:
        print("Too low, try again!")
    elif guess > secret_number:
        print("Too high, try again!")
    else:
        print(f"Correct! You guessed it in {attempts} attempts!")
