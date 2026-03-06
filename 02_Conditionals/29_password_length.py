"""
Simple conditional: Password strength by length
===============================================
Topic: Conditionals (02_Conditionals)
Description: Classify password as weak, okay, or strong.
"""

password = input("Enter password: ")
length = len(password)

if length < 6:
    strength = "Weak"
elif length < 10:
    strength = "Okay"
else:
    strength = "Strong"

print(f"Length: {length} → {strength}")
