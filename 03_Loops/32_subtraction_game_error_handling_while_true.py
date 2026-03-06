import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# ensure number1 >= number2
if number1 < number2:
    number1, number2 = number2, number1

correct_answer = number1 - number2
attempts = 0
max_attempts = 3

print("You have", max_attempts, "attempts")

while True:
    try:
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

    except ValueError:
        print("Invalid input. Please enter a number.")
