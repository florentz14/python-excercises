# -------------------------------------------------
# File Name: 03_strings.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Strings with single/double quotes, concatenation,
# -------------------------------------------------

name = "Python"
message = "Hello, world!"
print(name)
print(message)

# Multiline strings with triple quotes
paragraph = """This is a text
that spans multiple lines."""
print(paragraph)

# Concatenation with + and repetition with *
greeting = "Hello " + name
print(greeting)
print("=" * 20)

# Access by index (first is 0)
print("First character:", name[0])
print("Last character:", name[-1])

# Slicing [start:end:step]
print("First 3:", name[:3])
print("Last 2:", name[-2:])

# Common methods
text = "  Python is great  "
print("upper():", text.upper())
print("lower():", text.lower())
print("strip():", text.strip())
print("lstrip():", text.lstrip())
print("rstrip():", text.rstrip())
print("find():", text.find("is"))
print("count():", text.count("e"))
print("startswith():", text.startswith("Python"))
print("endswith():", text.endswith("Python"))
print("isalpha():", text.isalpha())
print("isdigit():", text.isdigit())
print("isspace():", text.isspace())
print("isalnum():", text.isalnum())
print("isupper():", text.isupper())
print("islower():", text.islower())
print("replace():", text.replace("great", "excellent"))
print("split():", "one,two,three".split(","))

# Length with len()
print("Length of name:", len(name))
