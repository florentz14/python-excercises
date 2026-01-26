# Simple While Loop Program
# This program demonstrates basic while loop examples

# Example 1: Count from 1 to 5
print("Example 1: Count from 1 to 5")
print("-" * 40)
count = 1
while count <= 5:
    print(count)
    count += 1

# Example 2: User input validation
print("\nExample 2: Input validation (enter 'quit' to exit)")
print("-" * 40)
while True:
    user_input = input("Enter a command: ")
    if user_input == "quit":
        print("Goodbye!")
        break
    else:
        print(f"You entered: {user_input}")

# Example 3: Sum numbers until user stops
print("\nExample 3: Sum numbers (enter -1 to stop)")
print("-" * 40)
total = 0
while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    total += num
print(f"Total sum: {total}")

# Example 4: Print countdown
print("\nExample 4: Countdown from 5")
print("-" * 40)
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blastoff!")

# Example 5: Find a number in range
print("\nExample 5: Guess the number (1-10)")
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

# Example 6: Print multiplication table with while loop
print("\nExample 6: Multiplication table of 3")
print("-" * 40)
i = 1
while i <= 10:
    print(f"3 × {i} = {3 * i}")
    i += 1

# Example 7: Nested while loops
print("\nExample 7: Nested while loops pattern")
print("-" * 40)
outer = 1
while outer <= 3:
    inner = 1
    while inner <= outer:
        print("*", end="")
        inner += 1
    print()
    outer += 1
