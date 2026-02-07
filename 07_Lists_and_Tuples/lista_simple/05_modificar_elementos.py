# ---------------------------------------------------------------------------
# Lista Simple - 05: Modificar Elementos
# ---------------------------------------------------------------------------
# Descripcion: Las listas son mutables, lo que permite cambiar elementos
#              individuales por indice o reemplazar secciones completas
#              usando slicing.
# Sintaxis:    lista[indice] = nuevo_valor
#              lista[inicio:fin] = [nuevos_valores]
# ---------------------------------------------------------------------------

# --- Cambiar un solo elemento por indice ---
fruits = ["apple", "banana", "cherry", "pineapple", "grape", "blueberry", "mango"]
print("Original:", fruits)

fruits[1] = "blackberry"  # Replace "banana" with "blackberry"
print("After fruits[1] = 'blackberry':", fruits)
# Output: ['apple', 'blackberry', 'cherry', 'pineapple', 'grape', 'blueberry', 'mango']

# --- Reemplazar una seccion (slice) con la misma cantidad de elementos ---
fruits[1:3] = ["blackcurrant", "watermelon"]  # Replace indices 1 and 2
print("After fruits[1:3] = ['blackcurrant', 'watermelon']:", fruits)
# Output: ['apple', 'blackcurrant', 'watermelon', 'pineapple', 'grape', 'blueberry', 'mango']

# --- Reemplazar una seccion con MENOS elementos (la lista se reduce) ---
fruits[1:3] = ["watermelon"]  # 2 elements replaced by 1
print("After fruits[1:3] = ['watermelon']:", fruits)
# Output: ['apple', 'watermelon', 'pineapple', 'grape', 'blueberry', 'mango']
print("Current length:", len(fruits))
# Output: 6

# --- Reemplazar una seccion con MAS elementos (la lista se expande) ---
fruits[1:2] = ["kiwi", "papaya", "dragonfruit"]  # 1 element replaced by 3
print("After fruits[1:2] = ['kiwi', 'papaya', 'dragonfruit']:", fruits)
# Output: ['apple', 'kiwi', 'papaya', 'dragonfruit', 'pineapple', 'grape', 'blueberry', 'mango']
print("Current length:", len(fruits))
# Output: 8

# --- Insertar elementos sin eliminar (slice vacio) ---
numeros = [1, 2, 5, 6]
numeros[2:2] = [3, 4]  # Insertar 3 y 4 en la posicion del indice 2
print("Insert with empty slice:", numeros)
# Output: [1, 2, 3, 4, 5, 6]

# --- Cambiar el ultimo elemento ---
fruits[-1] = "strawberry"
print("Change last element:", fruits)

# ---------------------------------------------------------------------------
# Nota: Asignar una lista vacia a un slice ELIMINA esos elementos.
# ---------------------------------------------------------------------------
ejemplo = [1, 2, 3, 4, 5]
ejemplo[1:4] = []  # Elimina los indices 1, 2, 3
print("Despues de ejemplo[1:4] = []:", ejemplo)
# Output: [1, 5]
