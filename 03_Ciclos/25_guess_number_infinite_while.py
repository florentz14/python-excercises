import random

# generate the random number
number = random.randint(0, 100)

print("Guess the hidden number between 0 and 100")

# initial value for guess
guess = -1

# loop until the user guesses the number
while guess != number:
    guess = int(input("Guess your number: "))

    if guess == number:
        print("Yes, you got it right!", number)
    elif guess > number:
        print("Your guess is high")
    else:
        print("Your guess is low")
