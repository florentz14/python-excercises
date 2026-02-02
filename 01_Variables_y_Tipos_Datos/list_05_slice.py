"""
Listas - Ejemplo 5: Rebanar (slice) una lista
=============================================
Tema: Listas (01_Variables_y_Tipos_Datos)
Descripción: Obtiene sublistas con [inicio:fin], paso [::2] y reverso [::-1].
"""

print("Example 5: Slice a list")
print("-" * 40)
letters = ["a", "b", "c", "d", "e", "f"]
print("Original list:", letters)
print("First 3 elements:", letters[0:3])
print("Elements from index 2 to 4:", letters[2:5])
print("Every second element:", letters[::2])
print("Reverse list:", letters[::-1])
