# ---------------------------------------------------------------------------
# Lista Simple - 22: Metodo index()
# ---------------------------------------------------------------------------
# Descripcion: El metodo index() retorna el indice de la PRIMERA ocurrencia
#              de un valor. Si el valor no se encuentra, lanza ValueError.
#              Opcionalmente acepta inicio y fin para limitar la busqueda.
# Sintaxis:    lista.index(valor)
#              lista.index(valor, inicio)
#              lista.index(valor, inicio, fin)
# Complejidad: O(n)
# ---------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "pineapple", "banana", "grape", "mango"]

# Encontrar la posicion de "cherry"
pos = fruits.index("cherry")
print(f"'cherry' is at index: {pos}")
# Output: 'cherry' is at index: 2

# Encontrar la primera "banana"
pos_banana = fruits.index("banana")
print(f"First 'banana' at index: {pos_banana}")
# Output: First 'banana' at index: 1

# Buscar "banana" despues del indice 2
pos_banana2 = fruits.index("banana", 2)
print(f"Second 'banana' at index: {pos_banana2}")
# Output: Second 'banana' at index: 4

# ---------------------------------------------------------------------------
# Error: ValueError si el elemento no existe
# ---------------------------------------------------------------------------
try:
    fruits.index("pear")
except ValueError as e:
    print(f"\nError: {e}")
# Output: Error: 'pear' is not in list

# ---------------------------------------------------------------------------
# Buena practica: verificar antes de buscar
# ---------------------------------------------------------------------------
search = "pineapple"
if search in fruits:
    print(f"\n'{search}' found at index {fruits.index(search)}")
else:
    print(f"\n'{search}' is not in the list")

# ---------------------------------------------------------------------------
# Encontrar TODAS las posiciones de un valor
# ---------------------------------------------------------------------------
numeros = [5, 3, 8, 3, 1, 3, 9, 3]
valor = 3

posiciones = []
inicio = 0
while True:
    try:
        pos = numeros.index(valor, inicio)
        posiciones.append(pos)
        inicio = pos + 1
    except ValueError:
        break

print(f"\nTodas las posiciones de {valor}: {posiciones}")
# Output: Todas las posiciones de 3: [1, 3, 5, 7]

# Alternativa con enumerate (mas limpio)
posiciones2 = [i for i, x in enumerate(numeros) if x == valor]
print(f"Con enumerate: {posiciones2}")
# Output: [1, 3, 5, 7]
