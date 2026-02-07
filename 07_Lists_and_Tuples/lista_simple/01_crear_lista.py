# ---------------------------------------------------------------------------
# Lista Simple - 01: Crear una Lista
# ---------------------------------------------------------------------------
# Descripcion: Una lista es una coleccion ordenada y mutable de elementos.
#              Se define usando corchetes [] y puede contener cualquier tipo
#              de dato. Los elementos se separan por comas.
# Metodo:      list literal [] / list()
# ---------------------------------------------------------------------------

# Create a list of fruits
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
