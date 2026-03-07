# Operator Precedence in Python

# Precedence order: () > ** > * / // % > + - > << >> & > ^ | > <= < > >= > == != > = %= /= //= -= += *= **= > and > or

# Example 1: Multiplication before addition
result1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {result1}")  # 14, not 20

# Example 2: Parentheses change precedence
result2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result2}")  # 20

# Example 3: Exponentiation before multiplication
result3 = 2 * 3 ** 2
print(f"2 * 3 ** 2 = {result3}")  # 18, not 36

# Example 4: Comparison before logical
result4 = 5 > 3 and 2 < 4
print(f"5 > 3 and 2 < 4 = {result4}")  # True

# Example 5: Logical AND before OR
result5 = True or False and False
print(f"True or False and False = {result5}")  # True

# Example 6: Using parentheses for clarity
result6 = (True or False) and False
print(f"(True or False) and False = {result6}")  # False