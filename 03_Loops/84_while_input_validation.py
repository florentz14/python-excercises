# -------------------------------------------------
# File Name: 84_while_input_validation.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Input validation (quit to exit).
# -------------------------------------------------

print("Example: Input validation (enter 'quit' to exit)")
print("-" * 40)

while True:
    user_input = input("Enter a command: ")
    if user_input == "quit":
        print("Goodbye!")
        break
    print(f"You entered: {user_input}")
