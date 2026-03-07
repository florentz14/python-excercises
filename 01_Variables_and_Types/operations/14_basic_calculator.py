# Basic Calculator in Python

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def calculator():
    print("Basic Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter operation choice (1-4): "))

        if choice not in [1, 2, 3, 4]:
            print("Invalid choice!")
            return

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = add(num1, num2)
            operation = "+"
        elif choice == 2:
            result = subtract(num1, num2)
            operation = "-"
        elif choice == 3:
            result = multiply(num1, num2)
            operation = "*"
        elif choice == 4:
            result = divide(num1, num2)
            operation = "/"

        print(f"{num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input! Please enter numbers.")


# Test the calculator functions
print("Testing calculator functions:")
print(f"5 + 3 = {add(5, 3)}")
print(f"10 - 4 = {subtract(10, 4)}")
print(f"6 * 7 = {multiply(6, 7)}")
print(f"15 / 3 = {divide(15, 3)}")
print(f"10 / 0 = {divide(10, 0)}")

# Uncomment the line below to run the interactive calculator
# calculator()
