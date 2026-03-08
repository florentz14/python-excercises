# -------------------------------------------------
# File Name: 35_password_check.py
# Description: Check password (case insensitive)
# -------------------------------------------------

PASSWORD = "password"
user_input = input("Enter password: ")
if user_input.casefold() == PASSWORD.casefold():
    print("Password correct.")
else:
    print("Incorrect password.")
