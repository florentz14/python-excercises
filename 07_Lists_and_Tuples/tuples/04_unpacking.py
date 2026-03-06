# ---------------------------------------------------------------------------
# Tuplas - 04: Unpack Tuples (Desempaquetar Tuplas)
# ---------------------------------------------------------------------------
# Description: Unpacking means extracting tuple values into individual
#              variables. The number of variables must match the number of
#              elements, unless you use the asterisk (*) operator.
# Syntax:      a, b, c = my_tuple
#              a, *b, c = my_tuple  (b gets remaining as a list)
# ---------------------------------------------------------------------------

# --- Basic unpacking ---
fruits = ("apple", "banana", "cherry")

# Assign each value to a variable
fruit1, fruit2, fruit3 = fruits

print("fruit1:", fruit1)  # apple
print("fruit2:", fruit2)  # banana
print("fruit3:", fruit3)  # cherry

# --- Unpacking with numbers ---
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"\nCoordinates: x={x}, y={y}, z={z}")
# Output: Coordinates: x=10, y=20, z=30

# ---------------------------------------------------------------------------
# Error: number of variables must match tuple length
# ---------------------------------------------------------------------------
try:
    a, b = fruits  # 3 values, 2 variables -> error
except ValueError as e:
    print(f"\nError: {e}")
# Output: Error: too many values to unpack (expected 2)

# =========================================================================
# Using asterisk (*) to collect remaining values
# =========================================================================

fruits = ("apple", "banana", "cherry", "pineapple", "grape", "mango")

# * collects the remaining values into a LIST
first, second, *rest = fruits
print("\nfirst:", first)    # apple
print("second:", second)  # banana
print("rest:", rest)      # ['cherry', 'pineapple', 'grape', 'mango']

# * in the middle
first, *middle, last = fruits
print("\nfirst:", first)    # apple
print("middle:", middle)  # ['banana', 'cherry', 'pineapple', 'grape']
print("last:", last)      # mango

# * at the beginning
*beginning, second_last, last = fruits
print("\nbeginning:", beginning)    # ['apple', 'banana', 'cherry', 'pineapple']
print("second_last:", second_last)  # grape
print("last:", last)                # mango

# ---------------------------------------------------------------------------
# Practical uses of unpacking
# ---------------------------------------------------------------------------

# Swap variables without a temp variable
a, b = 10, 20
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a
print(f"After swap:  a={a}, b={b}")

# Unpacking in a for loop with enumerate
colors = ("red", "green", "blue")
for index, color in enumerate(colors):
    print(f"  [{index}] {color}")

# Unpacking function return values
def get_user():
    return ("Alice", 30, "alice@email.com")

name, age, email = get_user()
print(f"\nUser: {name}, age {age}, email: {email}")

# Ignore values with underscore
_, age_only, _ = get_user()
print(f"Age only: {age_only}")
