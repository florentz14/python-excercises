"""
if.py - Ejemplo 5: Comprobar login
==================================
Tema: Condicionales (02_Condicionales)
Descripción: if/else con and para usuario y contraseña.
"""

print("Example 5: Login Check")
print("-" * 40)
username = "admin"
password = "password123"

if username == "admin" and password == "password123":
    print("Login successful!")
else:
    print("Invalid username or password")
