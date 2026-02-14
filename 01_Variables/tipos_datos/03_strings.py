"""
Strings (cadenas de texto) en Python
=====================================
Tema: Variables (01_Variables_y_Tipos_Datos)
Descripción: Crear strings, comillas simples/dobles, concatenación,
indexación, slicing, métodos comunes (upper, lower, strip, split, replace).
"""
# Crear strings con comillas simples o dobles
nombre = "Python"
mensaje = 'Hola, mundo!'
print(nombre)
print(mensaje)

# Strings multilínea con triple comilla
parrafo = """Este es un texto
que ocupa varias líneas."""
print(parrafo)

# Concatenación con + y repetición con *
saludo = "Hola " + nombre
print(saludo)
print("=" * 20)

# Acceso por índice (el primero es 0)
print("Primer carácter:", nombre[0])
print("Último carácter:", nombre[-1])

# Slicing [inicio:fin:paso]
print("Primeros 3:", nombre[:3])
print("Últimos 2:", nombre[-2:])

# Métodos comunes
texto = "  Python es genial  "
print("upper():", texto.upper())
print("lower():", texto.lower())
print("strip():", texto.strip())
print("lstrip():", texto.lstrip())
print("rstrip():", texto.rstrip())
print("find():", texto.find("es"))
print("count():", texto.count("e"))
print("startswith():", texto.startswith("Python"))
print("endswith():", texto.endswith("Python"))
print("isalpha():", texto.isalpha())
print("isdigit():", texto.isdigit())
print("isspace():", texto.isspace())
print("isalnum():", texto.isalnum())
print("isupper():", texto.isupper())
print("islower():", texto.islower())
print("replace():", texto.replace("genial", "excelente"))
print("split():", "uno,dos,tres".split(","))

# Longitud con len()
print("Longitud de nombre:", len(nombre))
