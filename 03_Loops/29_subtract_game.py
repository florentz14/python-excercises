"""While loop: Subtraction quiz.
Math quiz; loops until user gives correct subtraction answer.
"""
# Author: Florentino Báez


import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# Ensure number1 >= number2 for valid subtraction
if number1 < number2:
    number1, number2 = number2, number1

answer = int(input("What is " + str(number1) + " - " + str(number2) + "? "))

while number1 - number2 != answer:
    print("You got the wrong answer")
    answer = int(input("What is " + str(number1) +
                 " - " + str(number2) + "? "))

print("Finally you got it!")
