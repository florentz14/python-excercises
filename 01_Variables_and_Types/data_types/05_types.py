# -------------------------------------------------
# File Name: 05_types.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: int, float, str, bool types; type() function;
# -------------------------------------------------

integer = 42
decimal = 3.14
print("int:", integer, "->", type(integer))
print("float:", decimal, "->", type(decimal))

# Strings and booleans
text = "Hello"
true_val = True
false_val = False
print("str:", text, "->", type(text))
print("bool:", true_val, "->", type(true_val))

# Check type with type()
print("\ntype(integer):", type(integer))

# Type conversion
num_str = "100"
num_int = int(num_str)
print("\nint('100'):", num_int)

num_float = float("3.14")
print("float('3.14'):", num_float)

str_num = str(42)
print("str(42):", str_num, "->", type(str_num))

# bool() - falsy values: 0, 0.0, "", None, [], ()
print("\nbool(1):", bool(1))
print("bool(0):", bool(0))
print("bool(''):", bool(""))
print("bool('hello'):", bool("hello"))
