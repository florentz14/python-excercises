"""
Tuplas - Ejemplo 4: Rebanar (slice) una tupla
=============================================
Tema: Tuplas (01_Variables_y_Tipos_Datos)
Descripción: Obtiene subtuplas con [inicio:fin], paso y reverso.
"""

print("Example 4: Slice a tuple")
print("-" * 40)
letters = ("a", "b", "c", "d", "e", "f")
print("Original tuple:", letters)
print("First 3 elements:", letters[0:3])
print("Elements from index 2 to 4:", letters[2:5])
print("Every second element:", letters[::2])
print("Reverse tuple:", letters[::-1])
