# ---------------------------------------------------------------------------
# Lista Simple - 23: Metodo clear()
# ---------------------------------------------------------------------------
# Descripcion: El metodo clear() elimina TODOS los elementos de la lista,
#              dejandola vacia. La variable sigue existiendo (a diferencia
#              de 'del lista' que elimina la variable).
# Sintaxis:    lista.clear()
# Complejidad: O(1)
# ---------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "pineapple", "grape", "mango"]
print("Before clear():", fruits)
print("Length:", len(fruits))

fruits.clear()
print("\nAfter clear():", fruits)
print("Length:", len(fruits))
# Output: []
# Output: 0

# La variable sigue existiendo, se puede reutilizar
fruits.append("strawberry")
print("After adding:", fruits)
# Output: ['strawberry']

# ---------------------------------------------------------------------------
# Diferencia entre clear(), del y reasignacion
# ---------------------------------------------------------------------------
# clear()        -> Vacia la lista, la variable sigue existiendo
# del lista[:]   -> Mismo efecto que clear()
# del lista      -> Elimina la variable completamente
# lista = []     -> Crea una nueva lista vacia (la anterior se pierde)

# Ejemplo de la diferencia con referencias
original = [1, 2, 3]
referencia = original  # Ambas apuntan al mismo objeto

# Opcion A: clear() - afecta ambas variables
original.clear()
print("\nDespues de clear():")
print("  original:", original)     # []
print("  referencia:", referencia)  # [] (tambien se vacio)

# Opcion B: reasignar - solo afecta una variable
original = [1, 2, 3]
referencia = original

original = []  # Crea un nuevo objeto
print("\nDespues de reasignar:")
print("  original:", original)     # []
print("  referencia:", referencia)  # [1, 2, 3] (sigue intacta)

# ---------------------------------------------------------------------------
# Uso practico: limpiar una lista temporal en un bucle
# ---------------------------------------------------------------------------
lotes = [[1, 2], [3, 4, 5], [6]]
buffer = []

for lote in lotes:
    buffer.clear()        # Limpiar antes de procesar
    buffer.extend(lote)   # Llenar con nuevos datos
    print(f"Procesando lote: {buffer} (suma: {sum(buffer)})")
