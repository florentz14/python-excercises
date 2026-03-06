# ---------------------------------------------------------------------------
# Lista Simple - 07: Metodo insert()
# ---------------------------------------------------------------------------
# Descripcion: El metodo insert() agrega un elemento en una posicion
#              especifica de la lista. Los elementos existentes se desplazan
#              a la derecha. Modifica la lista original (in-place).
# Sintaxis:    lista.insert(indice, elemento)
# Complejidad: O(n) - porque desplaza los elementos posteriores
# ---------------------------------------------------------------------------

fruits = ["apple", "cherry", "pineapple", "grape"]
print("Original:", fruits)

# Insertar "orange" en el indice 1
fruits.insert(1, "orange")
print("After insert(1, 'orange'):", fruits)
# Output: ['apple', 'orange', 'cherry', 'pineapple', 'grape']

# Insertar al inicio de la lista (indice 0)
fruits.insert(0, "strawberry")
print("After insert(0, 'strawberry'):", fruits)
# Output: ['strawberry', 'apple', 'orange', 'cherry', 'pineapple', 'grape']

# Insertar al final (usando len() como indice)
fruits.insert(len(fruits), "mango")
print("After insert(len, 'mango'):", fruits)
# Output: ['strawberry', 'apple', 'orange', 'cherry', 'pineapple', 'grape', 'mango']

# Insertar con indice negativo
fruits.insert(-1, "kiwi")
print("After insert(-1, 'kiwi'):", fruits)
# Output: ['strawberry', 'apple', 'orange', 'cherry', 'pineapple', 'grape', 'kiwi', 'mango']
# Nota: -1 inserta ANTES del ultimo elemento

# ---------------------------------------------------------------------------
# Diferencia entre insert() y append()
# ---------------------------------------------------------------------------
lista = [1, 2, 3]

# append() siempre agrega al final
lista.append(99)
print("append(99):", lista)    # [1, 2, 3, 99]

# insert() puede agregar en cualquier posicion
lista.insert(0, 0)
print("insert(0, 0):", lista)  # [0, 1, 2, 3, 99]

# ---------------------------------------------------------------------------
# Nota: Si el indice es mayor que la longitud, insert() agrega al final.
#       Si el indice es menor que -len(lista), insert() agrega al inicio.
# ---------------------------------------------------------------------------
numeros = [10, 20, 30]
numeros.insert(100, 40)  # indice 100 > len(3), se agrega al final
print("insert(100, 40):", numeros)
# Output: [10, 20, 30, 40]
