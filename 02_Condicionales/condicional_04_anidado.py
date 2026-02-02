"""
Condicional - Ejemplo 4: if anidado
===================================
Tema: Condicionales (02_Condicionales)
Descripción: Un if dentro de otro para decisiones en dos niveles.
"""

edad = 20
tiene_permiso = True

if edad >= 18:
    if tiene_permiso:
        print("Puedes entrar")
    else:
        print("Necesitas permiso")
else:
    print("Debes ser mayor de 18 años")
