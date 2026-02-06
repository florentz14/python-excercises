import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

if number1 < number2:
    number1, number2 = number2, number1

correct = number1 - number2
attempts = 0

while attempts < 3:
    answer = int(input(f"What is {number1} - {number2}? "))

    if answer == correct:
        print("Finally you got it!")
        break
    else:
        print("You got the wrong answer")
        attempts = attempts + 1

if attempts == 3:
    print("Out of attempts! The correct answer was:", correct)
