# -------------------------------------------------
# File Name: 104_password_until_correct.py
# Description: Ask password until correct
# -------------------------------------------------

PASSWORD = "password"
while True:
    user = input("Enter password: ")
    if user == PASSWORD:
        print("Correct.")
        break
    print("Incorrect. Try again.")
