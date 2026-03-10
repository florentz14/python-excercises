# -------------------------------------------------
# File Name: 05_types.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: int, float, str, bool types; type() function;
# -------------------------------------------------

# Define two variables for different data types
integer = 42
decimal = 3.14
print("int:", integer, "->", type(integer))
print("float:", decimal, "->", type(decimal))

# Define two variables for string and boolean data types
text = "Hello"
true_val = True
false_val = False
print("str:", text, "->", type(text))
print("bool:", true_val, "->", type(true_val))

# Print the type of the integer variable
print("\ntype(integer):", type(integer))

# Define a variable for string to integer conversion
num_str = "100"
num_int = int(num_str)
# Print the result of the string to integer conversion
print("\nint('100'):", num_int)
# Define a variable for string to float conversion

num_float = float("3.14")
print("float('3.14'):", num_float)

# Define a variable for integer to string conversion
str_num = str(42)
# Print the result of the integer to string conversion
print("str(42):", str_num, "->", type(str_num))

# Define two variables for boolean conversion
true_val = True
false_val = False
# Print the result of the boolean conversion
print("\nbool(1):", bool(1))
print("bool(0):", bool(0))
print("bool(''):", bool(""))
print("bool('hello'):", bool("hello"))
# Print the result of the boolean conversion
print("bool(true_val):", bool(true_val))
print("bool(false_val):", bool(false_val))
