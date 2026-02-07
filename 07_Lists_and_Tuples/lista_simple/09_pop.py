# ---------------------------------------------------------------------------
# Lista Simple - 09: Metodo pop()
# ---------------------------------------------------------------------------
# Descripcion: El metodo pop() elimina y RETORNA el elemento en un indice
#              dado. Si no se especifica indice, elimina el ultimo elemento.
#              Lanza IndexError si el indice esta fuera de rango.
# Sintaxis:    lista.pop()       -> elimina y retorna el ultimo
#              lista.pop(indice) -> elimina y retorna el del indice dado
# Complejidad: O(1) sin indice / O(n) con indice
# ---------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "pineapple", "grape", "mango"]
print("Original:", fruits)

# pop() sin argumento: elimina y retorna el ultimo elemento
last = fruits.pop()
print(f"Removed element: '{last}'")
print("List after pop():", fruits)
# Output: Removed element: 'mango'
# Output: ['apple', 'banana', 'cherry', 'pineapple', 'grape']

# pop(indice): elimina y retorna el elemento en indice 1
second = fruits.pop(1)
print(f"Removed from index 1: '{second}'")
print("List after pop(1):", fruits)
# Output: Removed from index 1: 'banana'
# Output: ['apple', 'cherry', 'pineapple', 'grape']

# pop(0): elimina y retorna el primer elemento
first = fruits.pop(0)
print(f"First element removed: '{first}'")
print("List after pop(0):", fruits)
# Output: First element removed: 'apple'
# Output: ['cherry', 'pineapple', 'grape']

# ---------------------------------------------------------------------------
# Diferencia clave entre pop() y remove()
# ---------------------------------------------------------------------------
# pop()    -> trabaja con INDICES, retorna el elemento eliminado
# remove() -> trabaja con VALORES, retorna None

ejemplo = [10, 20, 30, 40, 50]
valor_pop = ejemplo.pop(2)       # Elimina indice 2 y retorna 30
print(f"\npop(2) retorno: {valor_pop}, lista: {ejemplo}")

ejemplo2 = [10, 20, 30, 40, 50]
valor_remove = ejemplo2.remove(30)  # Elimina el valor 30, retorna None
print(f"remove(30) retorno: {valor_remove}, lista: {ejemplo2}")

# ---------------------------------------------------------------------------
# Error: IndexError si el indice no existe
# ---------------------------------------------------------------------------
try:
    fruits.pop(10)
except IndexError as e:
    print(f"\nError: {e}")
# Output: Error: pop index out of range

# ---------------------------------------------------------------------------
# Uso practico: implementar una pila (stack) con pop()
# ---------------------------------------------------------------------------
pila = []
pila.append("tarea 1")
pila.append("tarea 2")
pila.append("tarea 3")
print("\nPila:", pila)

while pila:
    tarea = pila.pop()  # Siempre saca el ultimo (LIFO)
    print(f"  Procesando: {tarea}")
# Output: Procesando: tarea 3, tarea 2, tarea 1
