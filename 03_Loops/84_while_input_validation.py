"""
While loop: Input validation (quit to exit).
Loop until user enters 'quit'; breaks on exit command.

# Author: Florentino Báez
"""

print("Example: Input validation (enter 'quit' to exit)")
print("-" * 40)

while True:
    user_input = input("Enter a command: ")
    if user_input == "quit":
        print("Goodbye!")
        break
    print(f"You entered: {user_input}")
