# Function dispatch with dictionaries

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y if y != 0 else "Cannot divide by zero"


# Function dispatch dictionary
operations = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}


def calculate(operation, x, y):
    func = operations.get(operation)
    if func:
        return func(x, y)
    else:
        return "Unknown operation"


# Usage
print("5 + 3 =", calculate('add', 5, 3))
print("10 - 4 =", calculate('subtract', 10, 4))
print("6 * 7 =", calculate('multiply', 6, 7))
print("15 / 3 =", calculate('divide', 15, 3))
print("8 ? 2 =", calculate('modulo', 8, 2))

# More advanced: dispatch based on type


def process_data(data):
    dispatch = {
        int: lambda x: f"Integer: {x * 2}",
        str: lambda x: f"String: {x.upper()}",
        list: lambda x: f"List length: {len(x)}",
        dict: lambda x: f"Dict keys: {list(x.keys())}"
    }

    func = dispatch.get(type(data))
    if func:
        return func(data)
    else:
        return f"Unsupported type: {type(data)}"


print(process_data(42))
print(process_data("hello"))
print(process_data([1, 2, 3]))
print(process_data({'a': 1, 'b': 2}))
