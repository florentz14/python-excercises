# -------------------------------------------------
# File Name: 29_password_length.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: Password strength by length
# -------------------------------------------------

password = input("Enter password: ")
length = len(password)

if length < 6:
    strength = "Weak"
elif length < 10:
    strength = "Okay"
else:
    strength = "Strong"

print(f"Length: {length} → {strength}")
