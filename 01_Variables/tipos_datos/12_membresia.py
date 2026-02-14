"""
Operadores de membresía: in y not in
=====================================
Tema: Variables (01_Variables_y_Tipos_Datos)
Descripción: Verificar si un elemento está en una secuencia (string, lista, etc).
"""
# in y not in con strings (subcadena)
texto = "Python es genial"
print("'es' in texto:", "es" in texto)
print("'Java' in texto:", "Java" in texto)
print("'xyz' not in texto:", "xyz" not in texto)

# Con caracteres
print("\n'P' in 'Python':", "P" in "Python")

# Con listas
numeros = [1, 2, 3, 4, 5]
print("\n3 in numeros:", 3 in numeros)
print("10 not in numeros:", 10 not in numeros)

# Aplicación: validar entrada
opciones_validas = ["s", "n", "si", "no"]
respuesta = "s"
if respuesta.lower() in opciones_validas:
    print("\nRespuesta válida")
