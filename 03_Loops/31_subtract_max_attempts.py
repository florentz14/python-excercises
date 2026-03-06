"""While True: Subtraction quiz with max attempts.
Uses while True with break on correct answer or max attempts reached.
"""
# Author: Florentino Báez


import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# Ensure number1 >= number2 for valid subtraction
if number1 < number2:
    number1, number2 = number2, number1

correct_answer = number1 - number2
attempts = 0
max_attempts = 3

print("You have", max_attempts, "attempts")

while True:
    answer = int(input(f"What is {number1} - {number2}? "))
    attempts = attempts + 1

    if answer == correct_answer:
        print("Correct! You got it.")
        break
    else:
        print("Wrong answer")

    if attempts == max_attempts:
        print("Out of attempts! The correct answer was:", correct_answer)
        break
