# Basic Math Menu

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


def main():
    while True:
        print("\nBasic Math Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Choose an operation (1-5): ")

        if choice == '5':
            break

        if choice in ['1', '2', '3', '4']:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue

            if choice == '1':
                print(f"Result: {add(a, b)}")
            elif choice == '2':
                print(f"Result: {subtract(a, b)}")
            elif choice == '3':
                print(f"Result: {multiply(a, b)}")
            elif choice == '4':
                print(f"Result: {divide(a, b)}")
        else:
            print("Invalid choice. Please choose 1-5.")


if __name__ == "__main__":
    main()
