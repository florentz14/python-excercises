# ---------------------------------------------------------------------------
# Lista Simple - 03: Longitud de una Lista (len)
# ---------------------------------------------------------------------------
# Descripcion: La funcion len() devuelve la cantidad de elementos en una
#              lista. Es util para validaciones, bucles y comprobaciones.
# Sintaxis:    len(lista)
# ---------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "pineapple", "grape", "blueberry", "mango", "strawberry", "kiwi"]

# Obtener la longitud de la lista
print("Number of fruits:", len(fruits))
# Output: 9

# Usar len() para verificar si una lista esta vacia
lista_vacia = []
if len(lista_vacia) == 0:
    print("La lista esta vacia")
# Output: La lista esta vacia

# Forma mas pytonica de verificar si esta vacia
if not lista_vacia:
    print("La lista esta vacia (forma pytonica)")
# Output: La lista esta vacia (forma pytonica)

# Usar len() para acceder al ultimo elemento
last_index = len(fruits) - 1
print(f"Last index: {last_index} -> {fruits[last_index]}")
# Output: Last index: 8 -> kiwi

# Usar len() en una condicion
numeros = [10, 20, 30, 40, 50]
if len(numeros) >= 3:
    print(f"La lista tiene {len(numeros)} elementos (suficientes para procesar)")
# Output: La lista tiene 5 elementos (suficientes para procesar)

# Comparar longitudes de dos listas
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 7, 8]
print(f"Lista A: {len(lista_a)} elementos, Lista B: {len(lista_b)} elementos")
print(f"La lista mas larga tiene {max(len(lista_a), len(lista_b))} elementos")
# Output: La lista mas larga tiene 5 elementos
