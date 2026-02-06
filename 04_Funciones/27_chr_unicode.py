# 27_chr_unicode.py
# Demonstrates the chr() function - converts Unicode code to character

def code_to_char(code):
    """Converts a Unicode code point to its corresponding character."""
    return chr(code)

def show_char_range(start, end):
    """Displays characters for a range of Unicode codes."""
    print(f"Characters from code {start} to {end}:")
    for code in range(start, end + 1):
        print(f"  {code} -> '{chr(code)}'")

def print_alphabet_uppercase():
    """Prints A-Z using chr() with codes 65-90."""
    print("Uppercase alphabet (A-Z):")
    for code in range(65, 91):  # A=65, Z=90
        print(chr(code), end=" ")
    print()

def print_alphabet_lowercase():
    """Prints a-z using chr() with codes 97-122."""
    print("Lowercase alphabet (a-z):")
    for code in range(97, 123):  # a=97, z=122
        print(chr(code), end=" ")
    print()

def print_digits():
    """Prints 0-9 using chr() with codes 48-57."""
    print("Digits (0-9):")
    for code in range(48, 58):  # 0=48, 9=57
        print(chr(code), end=" ")
    print()

# Main execution
print("=== chr() Function Demo ===\n")

# Basic usage
print("1. Basic chr() examples:")
print(f"   chr(65) = '{chr(65)}'")   # A
print(f"   chr(97) = '{chr(97)}'")   # a
print(f"   chr(48) = '{chr(48)}'")   # 0
print(f"   chr(33) = '{chr(33)}'")   # !
print()

# Using our function
print("2. Using code_to_char() function:")
print(f"   code_to_char(72) = '{code_to_char(72)}'")  # H
print(f"   code_to_char(105) = '{code_to_char(105)}'")  # i
print()

# Alphabets
print("3. Generating alphabets:")
print_alphabet_uppercase()
print_alphabet_lowercase()
print()

# Digits
print("4. Generating digits:")
print_digits()
print()

# Special characters
print("5. Special characters:")
show_char_range(33, 47)  # ! " # $ % & ' ( ) * + , - . /
print()

# Build a word from codes
print("6. Building words from Unicode codes:")
codes = [72, 101, 108, 108, 111]  # H, e, l, l, o
word = ''.join(chr(c) for c in codes)
print(f"   Codes {codes} -> '{word}'")
