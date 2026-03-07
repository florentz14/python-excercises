# Division Types in Python

# Regular division (float division)
a = 10
b = 3
print(f"Regular division: {a} / {b} = {a / b} (type: {type(a / b)})")

# Floor division (integer division)
print(f"Floor division: {a} // {b} = {a // b} (type: {type(a // b)})")

# Modulus (remainder)
print(f"Modulus: {a} % {b} = {a % b}")

# Examples with different numbers
x = 17
y = 5
print(f"\n{x} / {y} = {x / y}")
print(f"{x} // {y} = {x // y}")
print(f"{x} % {y} = {x % y}")

# Negative numbers
m = -17
n = 5
print(f"\n{m} / {n} = {m / n}")
print(f"{m} // {n} = {m // n}")
print(f"{m} % {n} = {m % n}")

# Checking division properties
# For any a, b (b != 0): (a // b) * b + (a % b) = a
a = 17
b = 5
quotient = a // b
remainder = a % b
print(
    f"\nVerification: ({a} // {b}) * {b} + ({a} % {b}) = {quotient * b + remainder}")
print(f"Original: {a}")

# Float floor division
p = 10.5
q = 3.0
print(f"\n{p} // {q} = {p // q}")
print(f"{p} % {q} = {p % q}")
