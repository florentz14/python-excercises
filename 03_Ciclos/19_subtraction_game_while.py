import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# ensure number1 >= number2
if number1 < number2:
    number1, number2 = number2, number1

answer = int(input("What is " + str(number1) + " - " + str(number2) + "? "))

while number1 - number2 != answer:
    print("You got the wrong answer")
    answer = int(input("What is " + str(number1) +
                 " - " + str(number2) + "? "))

print("Finally you got it!")
