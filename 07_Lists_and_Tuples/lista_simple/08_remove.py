# ---------------------------------------------------------------------------
# Lista Simple - 08: Metodo remove()
# ---------------------------------------------------------------------------
# Descripcion: El metodo remove() elimina la PRIMERA ocurrencia de un valor
#              especifico de la lista. Si el valor no existe, lanza un
#              ValueError.
# Sintaxis:    lista.remove(valor)
# Complejidad: O(n) - busca el elemento y desplaza los posteriores
# ---------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "banana", "grape", "blueberry"]
print("Original:", fruits)

# Eliminar la primera ocurrencia de "banana"
fruits.remove("banana")
print("After remove('banana'):", fruits)
# Output: ['apple', 'cherry', 'banana', 'grape', 'blueberry']
# Nota: solo se elimino la PRIMERA "banana", la segunda sigue ahi

# Eliminar "cherry"
fruits.remove("cherry")
print("After remove('cherry'):", fruits)
# Output: ['apple', 'banana', 'grape', 'blueberry']

# ---------------------------------------------------------------------------
# Error comun: ValueError si el elemento no existe
# ---------------------------------------------------------------------------
try:
    fruits.remove("pear")
except ValueError as e:
    print(f"Error: {e}")
# Output: Error: list.remove(x): x not in list

# ---------------------------------------------------------------------------
# Buena practica: verificar si existe antes de eliminar
# ---------------------------------------------------------------------------
if "grape" in fruits:
    fruits.remove("grape")
    print("'grape' was removed:", fruits)
else:
    print("'grape' is not in the list")

# ---------------------------------------------------------------------------
# Eliminar TODAS las ocurrencias de un valor
# ---------------------------------------------------------------------------
numeros = [1, 3, 2, 3, 4, 3, 5]
print("\nOriginal numeros:", numeros)

while 3 in numeros:
    numeros.remove(3)
print("Despues de eliminar todos los 3:", numeros)
# Output: [1, 2, 4, 5]

# Alternativa con list comprehension (mas eficiente)
numeros2 = [1, 3, 2, 3, 4, 3, 5]
numeros2 = [x for x in numeros2 if x != 3]
print("Con list comprehension:", numeros2)
# Output: [1, 2, 4, 5]
