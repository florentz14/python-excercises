# ---------------------------------------------------------------------------
# Lista Simple - 18: Concatenar Listas (Operador +)
# ---------------------------------------------------------------------------
# Descripcion: El operador + permite unir (concatenar) dos o mas listas
#              creando una NUEVA lista. Las listas originales no se
#              modifican.
# Sintaxis:    lista3 = lista1 + lista2
# ---------------------------------------------------------------------------

lista1 = ["a", "b", "c"]
lista2 = [1, 2, 3]

# --- Concatenar dos listas ---
lista3 = lista1 + lista2
print("lista1 + lista2:", lista3)
# Output: ['a', 'b', 'c', 1, 2, 3]

# Las originales no cambian
print("lista1:", lista1)  # ['a', 'b', 'c']
print("lista2:", lista2)  # [1, 2, 3]

# --- Concatenar multiples listas ---
letras = ["x", "y"]
numeros = [7, 8]
simbolos = ["!", "@"]

combinada = letras + numeros + simbolos
print("\nMultiple:", combinada)
# Output: ['x', 'y', 7, 8, '!', '@']

# --- Usar += para agregar a una lista existente ---
fruits = ["apple", "banana"]
print("\nOriginal:", fruits)

fruits += ["cherry", "pear"]
print("After +=:", fruits)
# Output: ['apple', 'banana', 'cherry', 'pear']

# --- Repetir una lista con * ---
patron = [0, 1]
repetido = patron * 4
print("\n[0, 1] * 4:", repetido)
# Output: [0, 1, 0, 1, 0, 1, 0, 1]

# --- Uso practico: construir una lista separadora ---
separador = ["-"] * 10
contenido = ["inicio"] + separador + ["fin"]
print("\nCon separador:", contenido)
# Output: ['inicio', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'fin']

# ---------------------------------------------------------------------------
# Nota: El operador + siempre crea una nueva lista. Para agregar
#       elementos a una lista existente de forma mas eficiente,
#       usa extend() (ver archivo 20_extend.py).
# ---------------------------------------------------------------------------
