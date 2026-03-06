# ---------------------------------------------------------------------------
# Lista Simple - 10: Palabra Clave del
# ---------------------------------------------------------------------------
# Descripcion: La palabra clave 'del' permite eliminar elementos por indice,
#              eliminar secciones (slices), o eliminar la lista completa de
#              memoria. A diferencia de pop(), NO retorna el valor eliminado.
# Sintaxis:    del lista[indice]
#              del lista[inicio:fin]
#              del lista
# ---------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "pineapple", "grape", "blueberry", "mango"]
print("Original:", fruits)

# --- Eliminar un elemento por indice ---
del fruits[0]  # Elimina el primer elemento
print("After del fruits[0]:", fruits)
# Output: ['banana', 'cherry', 'pineapple', 'grape', 'blueberry', 'mango']

# --- Eliminar un rango (slice) ---
del fruits[1:3]  # Elimina indices 1 y 2
print("After del fruits[1:3]:", fruits)
# Output: ['banana', 'grape', 'blueberry', 'mango']

# --- Eliminar con paso ---
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del numeros[::2]  # Elimina los indices pares (0, 2, 4, 6, 8)
print("Eliminar cada 2:", numeros)
# Output: [1, 3, 5, 7, 9]

# ---------------------------------------------------------------------------
# Diferencia entre del, pop() y remove()
# ---------------------------------------------------------------------------
# del lista[i]     -> Elimina por indice, NO retorna nada
# lista.pop(i)     -> Elimina por indice, SI retorna el valor
# lista.remove(x)  -> Elimina por valor, NO retorna nada

ejemplo = [10, 20, 30, 40, 50]
del ejemplo[2]      # Solo elimina, no retorna
print("del ejemplo[2]:", ejemplo)   # [10, 20, 40, 50]

# ---------------------------------------------------------------------------
# Vaciar una lista sin eliminarla de memoria
# ---------------------------------------------------------------------------
colors = ["red", "blue", "green"]
del colors[:]  # Elimina TODOS los elementos, pero la variable sigue existiendo
print("After del colors[:]:", colors)
# Output: []

# Alternativa: usar clear()
numbers = [1, 2, 3]
numbers.clear()
print("After clear():", numbers)
# Output: []

# ---------------------------------------------------------------------------
# Eliminar la lista COMPLETA de memoria
# ---------------------------------------------------------------------------
lista_temporal = [1, 2, 3]
del lista_temporal  # La variable deja de existir

try:
    print(lista_temporal)
except NameError as e:
    print(f"Error: {e}")
# Output: Error: name 'lista_temporal' is not defined
