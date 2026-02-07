# ---------------------------------------------------------------------------
# Lista Simple - 02: Acceso por Indices
# ---------------------------------------------------------------------------
# Descripcion: Cada elemento de una lista tiene un indice (posicion).
#              Los indices positivos empiezan en 0 desde la izquierda.
#              Los indices negativos empiezan en -1 desde la derecha.
# Sintaxis:    lista[indice]
# ---------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "pineapple", "grape", "blueberry", "mango", "strawberry"]
#          index:  0        1         2         3            4        5            6        7
#  negative index: -8      -7        -6        -5           -4       -3          -2       -1

# Acceder al primer elemento (indice 0)
print("First element:", fruits[0])
# Output: apple

# Acceder al tercer elemento (indice 2)
print("Third element:", fruits[2])
# Output: cherry

# Acceder al ultimo elemento usando indice negativo (-1)
print("Last element:", fruits[-1])
# Output: strawberry

# Acceder al penultimo elemento (-2)
print("Second to last:", fruits[-2])
# Output: mango

# Acceder al primer elemento con indice negativo
print("First (negative index):", fruits[-len(fruits)])
# Output: apple

# ---------------------------------------------------------------------------
# Verificar si un elemento existe antes de acceder
# ---------------------------------------------------------------------------
if "cherry" in fruits:
    indice = fruits.index("cherry")
    print(f"'cherry' is at index {indice}")
# Output: 'cherry' is at index 2

# ---------------------------------------------------------------------------
# Error comun: IndexError al acceder a un indice fuera de rango
# ---------------------------------------------------------------------------
try:
    print(fruits[10])  # indice 10 no existe
except IndexError as e:
    print(f"Error: {e}")
# Output: Error: list index out of range
