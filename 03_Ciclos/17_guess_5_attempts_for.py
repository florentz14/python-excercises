import random

number = random.randint(0, 100)

print("Guess the hidden number between 0 and 100")

for attempt in range(5):
    guess = int(input("Guess your number: "))

    if guess == number:
        print("Yes, you got it right!", number)
        break
    elif guess > number:
        print("Your guess is high")
    else:
        print("Your guess is low")

else:
    print("Game over! The number was:", number)
