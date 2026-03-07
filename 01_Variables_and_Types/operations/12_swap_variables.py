# Swap Variables in Python

# Method 1: Using a temporary variable
def swap_with_temp(a, b):
    print(f"Before swap: a = {a}, b = {b}")
    temp = a
    a = b
    b = temp
    print(f"After swap: a = {a}, b = {b}")
    return a, b

# Method 2: Using tuple unpacking (Pythonic way)


def swap_tuple(a, b):
    print(f"Before swap: a = {a}, b = {b}")
    a, b = b, a
    print(f"After swap: a = {a}, b = {b}")
    return a, b

# Method 3: Using arithmetic operations (for numbers only)


def swap_arithmetic(a, b):
    print(f"Before swap: a = {a}, b = {b}")
    a = a + b
    b = a - b
    a = a - b
    print(f"After swap: a = {a}, b = {b}")
    return a, b

# Method 4: Using XOR (for integers only)


def swap_xor(a, b):
    print(f"Before swap: a = {a}, b = {b}")
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"After swap: a = {a}, b = {b}")
    return a, b


# Test with integers
print("=== Swapping integers ===")
x, y = 5, 10
swap_with_temp(x, y)
print()
swap_tuple(x, y)
print()
swap_arithmetic(x, y)
print()
swap_xor(x, y)

# Test with strings
print("\n=== Swapping strings ===")
str1, str2 = "hello", "world"
swap_tuple(str1, str2)

# Test with lists
print("\n=== Swapping lists ===")
list1, list2 = [1, 2, 3], [4, 5, 6]
swap_tuple(list1, list2)

# Multiple variable swap
print("\n=== Multiple variable swap ===")
a, b, c = 1, 2, 3
print(f"Before: a={a}, b={b}, c={c}")
a, b, c = c, a, b
print(f"After: a={a}, b={b}, c={c}")
