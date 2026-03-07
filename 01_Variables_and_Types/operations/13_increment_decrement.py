# Increment and Decrement in Python

# Python doesn't have ++ or -- operators like other languages
# We use += 1 and -= 1 instead

# Increment
print("Increment examples:")
x = 5
print(f"Initial x: {x}")
x += 1  # Increment by 1
print(f"After x += 1: {x}")
x += 2  # Increment by 2
print(f"After x += 2: {x}")

# Decrement
print("\nDecrement examples:")
y = 10
print(f"Initial y: {y}")
y -= 1  # Decrement by 1
print(f"After y -= 1: {y}")
y -= 3  # Decrement by 3
print(f"After y -= 3: {y}")

# Pre and post increment simulation
print("\nSimulating pre and post increment:")
z = 5
print(f"z = {z}")
print(f"z += 1 returns: {z + 1}")  # Post-increment simulation
z += 1
print(f"z after += 1: {z}")

# Using in loops
print("\nUsing in loops:")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

print("\nUsing in for loops:")
for i in range(5):
    print(f"i: {i}")

# Increment with different values
print("\nIncrement with different values:")
num = 0
print(f"Start: {num}")
num += 5
print(f"After += 5: {num}")
num += 10
print(f"After += 10: {num}")

# Decrement in loops
print("\nCountdown:")
counter = 10
while counter > 0:
    print(f"Counter: {counter}")
    counter -= 1
print("Blast off!")

# Float increment/decrement
print("\nFloat increment/decrement:")
price = 10.50
print(f"Price: ${price}")
price += 0.50
print(f"After increase: ${price}")
price -= 0.25
print(f"After discount: ${price}")
