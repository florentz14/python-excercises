# ---------------------------------------------------------------------------
# Lista Simple - 06: Metodo append()
# ---------------------------------------------------------------------------
# Descripcion: El metodo append() agrega UN solo elemento al FINAL de la
#              lista. Modifica la lista original (in-place) y retorna None.
# Sintaxis:    lista.append(elemento)
# Complejidad: O(1) - tiempo constante
# ---------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]
print("Original:", fruits)

# Agregar un elemento al final
fruits.append("orange")
print("After append('orange'):", fruits)
# Output: ['apple', 'banana', 'cherry', 'orange']

# Agregar otro elemento
fruits.append("grape")
print("After append('grape'):", fruits)
# Output: ['apple', 'banana', 'cherry', 'orange', 'grape']

# ---------------------------------------------------------------------------
# Nota importante: append() agrega el elemento como UN SOLO objeto.
# Si agregas una lista, se agrega como lista anidada (no se "aplana").
# ---------------------------------------------------------------------------
fruits.append(["kiwi", "mango"])
print("After append(['kiwi', 'mango']):", fruits)
# Output: ['apple', 'banana', 'cherry', 'orange', 'grape', ['kiwi', 'mango']]
# El ultimo elemento es una lista completa, no dos elementos separados

# ---------------------------------------------------------------------------
# Ejemplo practico: construir una lista elemento por elemento
# ---------------------------------------------------------------------------
cuadrados = []
for i in range(1, 6):
    cuadrados.append(i ** 2)
print("Cuadrados:", cuadrados)
# Output: [1, 4, 9, 16, 25]

# ---------------------------------------------------------------------------
# Error comun: append() retorna None, NO la lista modificada
# ---------------------------------------------------------------------------
result = fruits.append("strawberry")
print("Return of append():", result)
# Output: None
print("But the list WAS modified:", "strawberry" in fruits)
# Output: True
