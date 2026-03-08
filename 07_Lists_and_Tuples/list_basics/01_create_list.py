# -------------------------------------------------
# File Name: 01_create_list.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Una lista es una coleccion ordenada y mutable de elementos.
# -------------------------------------------------

fruits = ["apple", "banana", "cherry", "pineapple", "grape", "blueberry", "mango", "strawberry", "kiwi"]
print("Fruit list:", fruits)
# Output: ['apple', 'banana', 'cherry', 'pineapple', 'grape', 'blueberry', 'mango', 'strawberry', 'kiwi']

# Crear una lista de numeros
numeros = [10, 20, 30, 40, 50]
print("Lista de numeros:", numeros)
# Output: [10, 20, 30, 40, 50]

# Crear una lista mixta (diferentes tipos de datos)
mixta = ["texto", 42, 3.14, True, None]
print("Lista mixta:", mixta)
# Output: ['texto', 42, 3.14, True, None]

# Crear una lista vacia
vacia = []
print("Lista vacia:", vacia)
# Output: []

# Crear una lista usando el constructor list()
desde_string = list("Python")
print("Lista desde string:", desde_string)
# Output: ['P', 'y', 't', 'h', 'o', 'n']

# Crear una lista desde un rango
desde_rango = list(range(1, 6))
print("Lista desde rango:", desde_rango)
# Output: [1, 2, 3, 4, 5]

# ---------------------------------------------------------------------------
# Nota: Las listas son MUTABLES, lo que significa que se pueden modificar
#       despues de ser creadas (agregar, eliminar, cambiar elementos).
# ---------------------------------------------------------------------------
