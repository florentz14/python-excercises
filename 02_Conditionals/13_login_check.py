# -------------------------------------------------
# File Name: 13_login_check.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: if/else con and para usuario y contraseña.
# -------------------------------------------------

print("Example 5: Login Check")
print("-" * 40)
username = "admin"
password = "password123"

if username == "admin" and password == "password123":
    print("Login successful!")
else:
    print("Invalid username or password")
