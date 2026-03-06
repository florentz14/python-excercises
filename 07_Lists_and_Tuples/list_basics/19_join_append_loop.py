# ---------------------------------------------------------------------------
# Lista Simple - 19: Unir Listas con Bucle y append()
# ---------------------------------------------------------------------------
# Descripcion: Se puede agregar cada elemento de una lista a otra usando
#              un bucle for con append(). Esto MODIFICA la lista original
#              (a diferencia del operador + que crea una nueva).
# Patron:      for x in lista2:
#                  lista1.append(x)
# ---------------------------------------------------------------------------

lista1 = ["a", "b", "c"]
lista2 = [1, 2, 3]

print("Antes:")
print("  lista1:", lista1)
print("  lista2:", lista2)

# --- Agregar cada elemento de lista2 a lista1 ---
for x in lista2:
    lista1.append(x)

print("\nDespues del bucle append:")
print("  lista1:", lista1)
# Output: ['a', 'b', 'c', 1, 2, 3]

# lista2 no se modifica
print("  lista2:", lista2)
# Output: [1, 2, 3]

# ---------------------------------------------------------------------------
# Uso practico: unir con condicion (solo agregar ciertos elementos)
# ---------------------------------------------------------------------------
aprobados = ["Ana", "Carlos"]
notas = [("Luis", 85), ("Maria", 45), ("Pedro", 92), ("Sara", 38)]

print("\nAprobados iniciales:", aprobados)

for nombre, nota in notas:
    if nota >= 60:
        aprobados.append(nombre)

print("Aprobados finales:", aprobados)
# Output: ['Ana', 'Carlos', 'Luis', 'Pedro']

# ---------------------------------------------------------------------------
# Uso practico: combinar listas eliminando duplicados
# ---------------------------------------------------------------------------
fruits1 = ["apple", "banana", "cherry"]
fruits2 = ["banana", "grape", "apple", "orange", "kiwi"]

for fruit in fruits2:
    if fruit not in fruits1:
        fruits1.append(fruit)

print("\nCombined without duplicates:", fruits1)
# Output: ['apple', 'banana', 'cherry', 'grape', 'orange', 'kiwi']

# ---------------------------------------------------------------------------
# Nota: Para simplemente unir dos listas completas, extend() es mas
#       eficiente y limpio (ver archivo 20_extend.py).
#       El bucle con append es util cuando necesitas logica adicional.
# ---------------------------------------------------------------------------
