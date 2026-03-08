# -------------------------------------------------
# File Name: 04_anidado.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: Un if dentro de otro para decisiones en dos niveles.
# -------------------------------------------------

edad = 20
tiene_permiso = True

if edad >= 18:
    if tiene_permiso:
        print("Puedes entrar")
    else:
        print("Necesitas permiso")
else:
    print("Debes ser mayor de 18 años")
