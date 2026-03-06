# ---------------------------------------------------------------------------
# Lista Simple - 04: Slicing (Rebanado)
# ---------------------------------------------------------------------------
# Descripcion: El slicing permite extraer una porcion (sublista) de la lista
#              original. Se usan dos puntos [:] para definir el rango.
# Sintaxis:    lista[inicio:fin]       -> desde inicio hasta fin-1
#              lista[inicio:fin:paso]  -> con un paso especifico
#              lista[:fin]             -> desde el principio hasta fin-1
#              lista[inicio:]          -> desde inicio hasta el final
# ---------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "pineapple", "grape", "blueberry", "mango", "strawberry"]
#       index:  0        1         2         3           4        5           6        7

# Slice desde indice 2 (incluido) hasta indice 5 (excluido)
print("fruits[2:5]:", fruits[2:5])
# Output: ['cherry', 'pineapple', 'grape']

# Slice desde el inicio hasta indice 4 (excluido)
print("fruits[:4]:", fruits[:4])
# Output: ['apple', 'banana', 'cherry', 'pineapple']

# Slice desde indice 2 hasta el final
print("fruits[2:]:", fruits[2:])
# Output: ['cherry', 'pineapple', 'grape', 'blueberry', 'mango', 'strawberry']

# Slice con indices negativos (ultimos 3 elementos)
print("fruits[-3:]:", fruits[-3:])
# Output: ['blueberry', 'mango', 'strawberry']

# Slice desde el inicio hasta el penultimo (excluir el ultimo)
print("fruits[:-1]:", fruits[:-1])
# Output: ['apple', 'banana', 'cherry', 'pineapple', 'grape', 'blueberry', 'mango']

# Slice con paso (cada 2 elementos)
print("fruits[::2]:", fruits[::2])
# Output: ['apple', 'cherry', 'grape', 'mango']

# Slice invertido (lista al reves)
print("fruits[::-1]:", fruits[::-1])
# Output: ['strawberry', 'mango', 'blueberry', 'grape', 'pineapple', 'cherry', 'banana', 'apple']

# Copiar toda la lista usando slicing
copy_list = fruits[:]
print("Full copy:", copy_list)

# ---------------------------------------------------------------------------
# Nota: El slicing NUNCA genera un IndexError, incluso si los indices
#       exceden el rango. Simplemente retorna lo que exista en ese rango.
# ---------------------------------------------------------------------------
print("fruits[2:100]:", fruits[2:100])
# Output: ['cherry', 'pineapple', 'grape', 'blueberry', 'mango', 'strawberry']
