# ---------------------------------------------------------------------------
# Lista Simple - 20: Metodo extend()
# ---------------------------------------------------------------------------
# Descripcion: El metodo extend() agrega todos los elementos de un iterable
#              al final de la lista. Modifica la lista original (in-place).
#              A diferencia de append(), no agrega el iterable como un solo
#              elemento, sino que "desempaqueta" cada elemento.
# Sintaxis:    lista.extend(iterable)
# Complejidad: O(k) donde k es el tamano del iterable agregado
# ---------------------------------------------------------------------------

lista1 = ["a", "b", "c"]
lista2 = [1, 2, 3]

print("Antes:")
print("  lista1:", lista1)
print("  lista2:", lista2)

# --- Extender lista1 con lista2 ---
lista1.extend(lista2)
print("\nDespues de extend():")
print("  lista1:", lista1)
# Output: ['a', 'b', 'c', 1, 2, 3]

# ---------------------------------------------------------------------------
# Diferencia entre append() y extend()
# ---------------------------------------------------------------------------
ejemplo_append = [1, 2, 3]
ejemplo_extend = [1, 2, 3]

ejemplo_append.append([4, 5, 6])
ejemplo_extend.extend([4, 5, 6])

print("\n--- append vs extend ---")
print("append([4,5,6]):", ejemplo_append)
# Output: [1, 2, 3, [4, 5, 6]]  <- lista anidada

print("extend([4,5,6]):", ejemplo_extend)
# Output: [1, 2, 3, 4, 5, 6]    <- elementos individuales

# ---------------------------------------------------------------------------
# extend() funciona con cualquier iterable (no solo listas)
# ---------------------------------------------------------------------------
numeros = [1, 2, 3]

# Extender con una tupla
numeros.extend((4, 5))
print("\nExtend con tupla:", numeros)
# Output: [1, 2, 3, 4, 5]

# Extender con un string (cada caracter es un elemento)
letras = ["a", "b"]
letras.extend("xyz")
print("Extend con string:", letras)
# Output: ['a', 'b', 'x', 'y', 'z']

# Extender con un range
secuencia = [0]
secuencia.extend(range(1, 6))
print("Extend con range:", secuencia)
# Output: [0, 1, 2, 3, 4, 5]

# Extender con un set (orden no garantizado)
base = [1, 2]
base.extend({3, 4, 5})
print("Extend con set:", base)

# ---------------------------------------------------------------------------
# Comparacion de metodos para combinar listas
# ---------------------------------------------------------------------------
# +         -> Crea nueva lista, no modifica originales
# append()  -> Agrega un solo elemento (puede ser otra lista como objeto)
# extend()  -> Agrega cada elemento individualmente, modifica in-place
# +=        -> Equivalente a extend() (modifica la lista original)

a = [1, 2]
a += [3, 4]  # Equivalente a a.extend([3, 4])
print("\n+= es como extend():", a)
# Output: [1, 2, 3, 4]
