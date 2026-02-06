# ---------------------------------------------------------------------------
# Part 1: Lists - Exercise 10
# ---------------------------------------------------------------------------
# Descripción: Pedir al usuario 3 números, guardarlos en una lista y
#              mostrar la suma de todos.
# ---------------------------------------------------------------------------

# Lista vacía donde guardaremos los números introducidos
nums = []
# Repetimos 3 veces: pedir un número y añadirlo a la lista
for i in range(3):
    # input() devuelve texto; int() lo convierte a número entero
    n = int(input('Enter a number: '))
    # append() añade el número al final de la lista
    nums.append(n)
# sum() suma todos los elementos de la lista; mostramos el resultado
print(sum(nums))
