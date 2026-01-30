import random

number = random.randint(0, 100)

print("Guess a number between 0 and 100")

while True:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Alright! You guessed", number)
        break
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
